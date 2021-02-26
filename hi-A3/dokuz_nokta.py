import turtle 

turtle.Screen().setup(600,600)
turtle.speed(2)
turtle.penup()
x=-200
y=200
turtle.pensize(10)

for i in range(3):#satır hareketi
    turtle.goto(x,y)
    for t in range(3):# noktaları çizecek
        turtle.dot()
        turtle.forward(50)
    y=y-50

turtle.done()