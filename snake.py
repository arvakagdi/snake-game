from turtle import Turtle

STARTING_POSITIONS  = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:  # setting up intial 3 blocks of snake
            segment = Turtle('square')
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
        
    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):   
            new_x = self.segments[num - 1].xcor()    # get x coord of prev elem
            new_y = self.segments[num - 1].ycor()    # get y coord of prev elem
            self.segments[num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)



