import turtle
turtle.colormode(255)
import random
class food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.speed(10)
        self.color("dark green")
        self.repeat()

    def repeat(self):
        self.goto(random.randrange(-230, 230, 20),random.randrange(-230, 230, 20))
