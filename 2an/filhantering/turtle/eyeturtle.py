from turtle import *
from random import randint
#förberedelser
width(6)
speed(0)
bgcolor("black")
pencolor("blue")

up()
backward(25)
left(90)
right(90)

down()
i = 0
while i <= 180:
    pencolor("black")
    forward(125)
    
    r = randint(1,3)
    if r == 1:
        pencolor("skyblue")
    elif r == 2:
        pencolor("lightgreen")
    elif r == 3:
        pencolor("yellow")
    forward(375)
    left(181)
    forward(375)
    pencolor("black")
    forward(125)
    i +=1
pencolor("black")
width(50)
left(180)
forward(75)
done()
hideturtle()