import colorgram
import turtle
from random import choice
turtle.colormode(255)
c=colorgram.extract('vib.jpg',30)
colors=[]
for i in c:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    colors.append((r,g,b))
# print(colors)

t=turtle.Turtle()
scrn=turtle.Screen()
t.pu()
t.ht()
# t.speed(100)
t.goto((250.00,-250.00))
for i in range(1,10):
    if i%2==0:
        t.right(90)
        t.forward(50)
        t.right(90)
    else:
        t.left(90)
        t.forward(50)
        t.left(90)
    for j in range(10):
        t.dot(15,choice(colors))
        t.forward(50,)
        t.dot(15,choice(colors))


scrn.exitonclick()