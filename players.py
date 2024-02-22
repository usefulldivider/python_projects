from turtle import Turtle
class players(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(pos)

    def move_up(self):
        if self.ycor() < 200:
            self.goto(self.xcor(),self.ycor() + 50)

    def move_down(self):
        if self.ycor() > -200:
            self.goto(self.xcor(),self.ycor() - 50)

    def getout(self):
        self.clear()