import turtle
from random import randint
scrn = turtle.Screen()
scrn.setup(width=500, height=500)
gameon=False
ubet = scrn.textinput(
    prompt="which of the teenage turtles do you think will win?\nturtles are:\nleonardo(blue),donatello(purple),michelangelo(orange),raphael(red)",
    title="Place your bet").lower()
y=-50
colors=["red","blue","orange","purple"]
turtles=[]
for i in range(0,4):
    t=turtle.Turtle(shape="turtle")
    t.pu()
    t.color(colors[i])
    t.goto(-230,y)
    y+=30
    turtles.append(t)

if ubet:
    gameon=True
while gameon:
    for i in turtles:
        i.forward(randint(1,10))
        if i.xcor()>=230:
            gameon=False
            winner=i

if ubet=="raphael" and winner.color()[0]=="red":
    print("Raphael won")
elif ubet=="leonardo" and winner.color()[0]=="blue":
    print("leonardo won")
elif ubet=="michelangelo" and winner.color()[0]=="orange":
    print("michelangelo won")
elif ubet=="donatello" and winner.color()[0]=="orange":
    print("donatello won")
else:
    print("Oh no your turtle lost \ntake this L")
scrn.exitonclick()

