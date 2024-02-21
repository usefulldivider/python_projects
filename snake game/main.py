import turtle
import time
import snake
import food
import scoreboard
turtle.colormode(255)
scrn=turtle.Screen()
scrn.title("turtle congo line")
scrn.setup(height=500,width=500)
scrn.bgcolor("light blue")
start=[(0,0),(-20,0),(-40,0)]
a=0
scrn.tracer(0)
s=snake.Snake()
f=food.food()
scr=scoreboard.scoreboard()
# scrn.update()

scrn.listen()
scrn.onkey(s.up, "w")
scrn.onkey(s.left, "a")
scrn.onkey(s.right, "d")
scrn.onkey(s.down, "s")

game_on=True
while game_on:
    scrn.update()
    time.sleep(.1)
    s.move()


    if s.snake[0].distance(f)<15:
        f.repeat()
        s.addseg()
        scr.scoreplus()

    if s.snake[0].xcor()>240 or s.snake[0].ycor()>240 or s.snake[0].xcor()<-250 or s.snake[0].ycor()<-240:
        print(s.snake[0].pos())
        scr.gover()
        game_on=False


    for i in s.snake[1:]:

        if s.snake[0].distance(i)<10:
            print(s.snake[0].pos())

            scr.gover()
            game_on = False




scrn.exitonclick()