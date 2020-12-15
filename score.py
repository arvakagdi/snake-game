from turtle import Turtle

POSITION = (0,260)
ALIGHMENT = "center"
FONT = ("Comic Sans MS", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.color("white")
        self.CurrScore = 0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f'Score: {self.CurrScore}', False, align = ALIGHMENT, font = FONT)
        self.CurrScore += 1