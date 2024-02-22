import turtle
import scoreboard
import players
import ball
import time
scrn=turtle.Screen()
scrn.title("Pong")
scrn.bgcolor("black")
scrn.setup(height=500,width=700)

#score
s=scoreboard.score()

# midline
midline=turtle.Turtle()
midline.pu()
midline.goto(0,210)
midline.setheading(270)
midline.color("white")
midline.width(5)
midline.hideturtle()
for i in range(1,25):
    midline.pd()
    midline.forward(10)
    midline.pu()
    midline.forward(10)


scrn.tracer(0)
#player 1'
p1=players.players((320,0))
p2=players.players((-320, 0))
scrn.listen()
scrn.onkey(p2.move_up,"w")
scrn.onkey(p2.move_down,"s")
scrn.onkey(p1.move_up,"Up")
scrn.onkey(p1.move_down,"Down")

b=ball.ball()
# scrn.update()
game_on=True
while game_on:

    scrn.update()
    time.sleep(b.mspeed)
    b.move()
    if s.p1 == 10 or s.p2 == 10:
        game_on=False
        time.sleep(2)
        exit()
    if b.xcor()>350 :
        s.scoreinc(1)
        b.start()
        b.bounce_X()
    elif b.xcor()<-350:
        s.scoreinc(2)
        b.start()
        b.bounce_X()

    if b.ycor()>240 or b.ycor()<-240:
        b.bounce_Y()
    if (b.distance(p1)<50 and b.xcor()>=310)or(b.distance(p2)<50 and b.xcor()<=-310):
        b.bounce_X()
scrn.exitonclick()