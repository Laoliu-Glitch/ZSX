from random import random,choice
from turtle import *

player = [0,-140]
ball = [0,140]
dire = [choice([-2,-1,1,2]),choice([-2,-1])]

def move(aim):
    player[0] += aim

def bounce():
    if ball[0] <= -300 or ball[0] >= 290:
        dire[0] = -dire[0]
    elif ball[1] >= 150:
        dire[1] = -dire[1]
    elif ball[1] <= -140+10+5 and player[0] <= ball[0] <= player[0] + 70:
        dire[1] = -dire[1]

def outside():
    if ball[1] <= -140:
        return True

def rectangle(x,y,width,height):
    up()
    goto(x,y)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    clear()
    up()
    goto(ball[0],ball[1])
    dot(10,"red")
    rectangle(player[0],player[1],70,10)
    update()

def gameLoop():
    bounce()
    ball[0] += dire[0]*2
    ball[1] += dire[1]*2
    draw()
    if outside():
        return
    ontimer(gameLoop,50)

setup(620,320,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda:move(20),'d')
onkey(lambda:move(-20),'a')
gameLoop()
done()    