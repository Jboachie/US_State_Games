from turtle import Turtle

class Statenames(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def state_name(self, answer, x, y):
        self.goto(x,y)
        self.write(answer, align = "center", font = ("Arial", 8, "normal"))
