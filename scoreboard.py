from turtle import Turtle
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,210)
        self.pu()
        self.hideturtle()
        self.p1=0
        self.p2=0
        self.color("light blue")
        self.write(arg=f"Score {self.p1}:{self.p2}",move=False,font=("Arial",20,"bold"),align="center")

    def scoreinc(self,i):
        """ increments score for the players send 1 for player 1,2 for player 2"""
        if i ==1:
            self.p1+=1
        elif i==2:
            self.p2+=1
        self.clear()
        self.write(arg=f"Score {self.p1}:{self.p2}",move=False,font=("Arial",20,"bold"),align="center")



