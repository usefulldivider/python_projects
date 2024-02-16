import turtle
from random import randint
turtle.colormode(255)
t=turtle.Turtle()
scrn=turtle.Screen()
scrn.listen()
t.width(3)
def move_f():
    t.forward(100)
    t.pencolor((randint(0,255),randint(0,255),randint(0,255)))
def move_b():
    t.backward(100)
    t.pencolor((randint(0,255),randint(0,255),randint(0,255)))

def clear_scr():
    t.home()
    t.clear()
def rot_l():
    t.left(45)

def rot_r():
    t.right(45)
scrn.onkey(fun=move_f,key="w")
scrn.onkey(fun=move_b,key="s")
scrn.onkey(fun=rot_l,key="a")
scrn.onkey(fun=rot_r,key="d")
scrn.onkey(fun=clear_scr,key="c")
scrn.exitonclick()