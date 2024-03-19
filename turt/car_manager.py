COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
from turtle import Turtle
import random as r
class CarManager:

    def __init__(self):
        self.allcars = []
        self.carspeed=STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2)
        car.color(r.choice(COLORS))
        car.pu()
        car.goto(300, r.randint(-200, 200))
        self.allcars.append(car)




    def movingcars(self):
        for i in self.allcars:
            i.backward(self.carspeed)
        
    def increment_speed(self):
        self.carspeed+=MOVE_INCREMENT




