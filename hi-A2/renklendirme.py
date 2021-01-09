import turtle
turtle.shape("turtle")
turtle.color("red","yellow")

turtle.pensize(4)
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.circle(100)



turtle.done()