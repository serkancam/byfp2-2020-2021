import turtle
import time
turtle.Screen().setup(600,600)
turtle.penup()
turtle.pensize(10)
x=-200
y=200 
for i in range(5):#0,1,2,3,4
    turtle.goto(x,y)
    for t in range(i+1):
        turtle.dot()
        turtle.forward(50)
    y=y-50

turtle.done()