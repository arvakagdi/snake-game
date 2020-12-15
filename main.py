from turtle import Turtle, Screen
from snake import Snake 
from food import Food
from score import Score
import time  # to add delays


screen = Screen()
screen.setup(width = 600, height = 600)   # size of screen
screen.bgcolor("pale turquoise")
screen.title("My Snake Game")
screen.tracer(0)    # stops tracing anything and won't display anthing on screen until we have screen update
 
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
# to have snake's proper movement when it turns, we will start updating from tail (3rd goes to 2nd --> 1 and 1 will change direction if needed)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:    # we check if snake and food's distance to detect collision
        food.refresh()
        snake.extend()       # increasing size of the snake
        score.updateScore()
    
    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.gameOver()

    # Detect collision with tail
    for seg in range(1,len(snake.segments)):
        if snake.head.distance(snake.segments[seg]) < 10:
            game_is_on = False
            score.gameOver()

screen.exitonclick()