from turtle import Turtle
import random

STARTING_POSITIONS  = [(0,0), (-20,0), (-40,0)]
COLORS = ['white', 'pink', 'lavender', 'light yellow', 'ivory', 'dark sea green', 'powder blue', 'pale goldenrod', 'thistle', 'light blue', 'light slate gray', 'burlywood', 'violet']
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # place this after create_snake else segments would still be empty

    def create_snake(self):
        for position in STARTING_POSITIONS:  # setting up intial 3 blocks of snake
            self.addSegment(position)

    def extend(self):
        self.addSegment(self.segments[-1].position())  # add an extra seg to the last pos

    def addSegment(self, position):
        segment = Turtle('circle')
        segment.color(random.choice(COLORS))
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)


        
    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):   
            new_x = self.segments[num - 1].xcor()    # get x coord of prev elem
            new_y = self.segments[num - 1].ycor()    # get y coord of prev elem
            self.segments[num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:    # head.heading() returns heading value of head
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!= UP:     # we can't go from up to down and same for all directions
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(0)