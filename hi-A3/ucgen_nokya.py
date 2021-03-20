import turtle

turtle.Screen().setup(600,600)
turtle.penup()
x = -200
y = 200
turtle.pensize(20)

for i in range(1,6):#satır hareketi
    turtle.goto(x,y)
    for t in range(i):# noktaları çizecek
        turtle.dot()
        turtle.forward(50)
    y=y-50

turtle.done()

