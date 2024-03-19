import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.bgpic("road.png")
p = Player()
cm = CarManager()
sc=scoreboard()
screen.onkeypress(p.move_up, "w")
screen.onkeypress(p.move_up, " ")

game_is_on = True
ins=turtle.Turtle()
ins.ht()
ins.pu()
ins.goto(0, 0)
ins.color("black")
ins.write(arg="Press W or space to move", move=False, align="center", font=("Courier", 24, "normal"))


while game_is_on:

    time.sleep(0.1)
    screen.update()
    if 1 == random.randint(1, 6):
        cm.create_car()
    cm.movingcars()
    for i in cm.allcars:
        if i.distance(p)<=20:
            game_is_on=False
            sc.gover()
    if p.ycor()>200:
        p.reset_player()
        sc.scoreplus()
        cm.increment_speed()

screen.exitonclick()
