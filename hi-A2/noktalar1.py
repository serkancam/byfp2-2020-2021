import turtle

turtle.Screen().setup(600,600)
turtle.pensize(10)
turtle.penup()
x=-200
y=200

for t in range(3):
    turtle.goto(x,y)
    for i in range(3):
        turtle.dot()
        turtle.forward(50)
    y=y-50
    

turtle.done()