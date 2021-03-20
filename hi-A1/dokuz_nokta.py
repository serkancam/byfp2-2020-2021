import turtle
import time

turtle.Screen().setup(600, 600)
turtle.pensize(10)
turtle.penup()
# turtle.dot()
x = -200
y = 200
# çözümleriniz satırın altına olacak
for i in range(1000,1003):
    turtle.goto(x,y)
    for s in range(9990,9993):
        turtle.dot()
        turtle.forward(50)
    y=y-50

turtle.done()
