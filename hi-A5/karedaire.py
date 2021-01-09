import turtle
turtle.shape("turtle")
turtle.speed(4)
turtle.penup()
turtle.goto(-220,-200)
turtle.pendown()
turtle.color("red","yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(80)
    turtle.left(72)
turtle.end_fill()

turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.pensize(4)
turtle.color("blue","#78281F")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.done()