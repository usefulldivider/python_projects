from turtle import Turtle
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.pu()
        self.home()
        self.xm=2
        self.ym=2

    def move(self):
        self.goto(self.xcor()+self.xm,self.ycor()+self.ym)

    def bounce_Y(self):
        self.ym *=-1

    def start(self):
        self.home()

    def bounce_X(self):
        self.xm *=-1
