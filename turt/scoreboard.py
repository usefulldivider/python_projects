FONT = ("Courier", 24, "normal")
import turtle

class scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(0,265)
        self.sc=0
        self.color("black")
        self.write(arg=f"SCORE:{self.sc}",move=False,align="center",font=FONT)

    def scoreplus(self):
        self.sc+=10
        self.clear()
        self.write(arg=f"SCORE:{self.sc}",move=False,align="center",font=FONT)

    def gover(self):
        self.clear()
        self.home()
        self.color("Dark blue")
        self.write(arg=f"Game over \nScore:{self.sc} ",move=False,align="center",font=FONT)