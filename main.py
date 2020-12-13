from turtle import Turtle, Screen
import time  # to add delays


screen = Screen()
screen.setup(width = 600, height = 600)   # size of screen
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)    # stops tracing anything and won't display anthing on screen until we have screen update
 
segment_positions  = [(0,0), (-20,0), (-40,0)]
segments = []

for position in segment_positions:  # setting up intial 3 blocks of snake
    segment = Turtle('square')
    segment.color("white")
    segment.penup()
    segment.setpos(position)
    segments.append(segment)

game_is_on = True


# to have snake's proper movement when it turns, we will start updating from tail (3rd goes to 2nd --> 1 and 1 will change direction if needed)
while game_is_on:

    screen.update()
    time.sleep(0.1)
    for num in range(len(segments) - 1, 0, -1):   
        new_x = segments[num - 1].xcor()    # get x coord of prev elem
        new_y = segments[num - 1].ycor()    # get y coord of prev elem
        segments[num].goto(new_x,new_y)

    segments[0].forward(20)
    segments[0].right(90)






screen.exitonclick()