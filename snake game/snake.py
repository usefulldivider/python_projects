import turtle
from random import randint

START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP=20



class Snake:
    def __init__(self):
        self.snake = []
        a = 0
        for i in START:
            segment = turtle.Turtle("turtle")
            segment.pu()
            if a == 0:
                segment.color("black")
            else:
                segment.color(randint(50, 255), randint(50, 255), randint(50, 255))
            a += 1
            segment.goto(i)
            self.snake.append(segment)
        self.head=self.snake[0]



    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
            self.snake[i].setheading(self.snake[i - 1].heading())
        self.snake[0].forward(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def addseg(self):
        segment = turtle.Turtle("turtle")

        segment.pu()
        segment.color(randint(50, 255), randint(50, 255), randint(50, 255))
        segment.goto(self.snake[-1].pos())
        self.snake.append(segment)
