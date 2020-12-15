from turtle import Turtle
import random

COLORS = [ 'yellow', 'navy', 'gainsboro', 'orange', 'goldenrod', 'dark goldenrod','lavender', 'silver', 'alice blue', 'gold', 'plum', 'navajo white', 'thistle', 'blanched almond', 'dark khaki']

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        # self.color('cyan')
        self.speed('fastest')
        self.refresh()  # create a food 
    
    def refresh(self):  
        self.color(random.choice(COLORS))  
        self.goto(random.randint(-280,280),random.randint(-280,280))
