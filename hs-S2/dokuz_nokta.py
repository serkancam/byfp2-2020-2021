import turtle 
import time
turtle.Screen().setup(600,600)
turtle.penup()
turtle.pensize(10)
# çözüm
x=-200
y=200
for i in range(3):
    turtle.goto(x,y)
    for t in range(3):
        turtle.dot()
        turtle.forward(50)
    y=y-50
turtle.done()