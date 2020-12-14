from turtle import Turtle, Screen
from snake import Snake 
from food import Food
import time  # to add delays


screen = Screen()
screen.setup(width = 600, height = 600)   # size of screen
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)    # stops tracing anything and won't display anthing on screen until we have screen update
 
snake = Snake()
food = Food()

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

    # Detech collision with food
screen.exitonclick()