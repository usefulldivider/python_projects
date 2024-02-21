import turtle
from random import randint
class scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(0,225)
        self.sc=0
        self.color("black")
        self.write(arg=f"Turts:{self.sc}",move=False,align="center",font=('Arial', 15, 'normal'))


    def scoreplus(self):
        self.sc+=1
        self.clear()
        self.write(arg=f"Turts:{self.sc}",move=False,align="center",font=('Arial', 15, 'normal'))

    def gover(self):
        self.clear()
        self.home()
        self.color("Dark blue")
        self.write(arg=f"Game over \nYou got {self.sc} turts",move=False,align="center",font=('Arial', 15, 'normal'))






