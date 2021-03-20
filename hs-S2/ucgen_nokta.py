import turtle
import time

turtle.Screen().setup(600,600)
turtle.pensize(10)
turtle.penup()
x=-200
y=200

for i in range(1,6):
    turtle.goto(x,y)
    for t in range(i):
        turtle.dot()
        turtle.forward(50)
    y=y-50


turtle.done()