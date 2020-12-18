import turtle
turtle.shape("turtle")
#beşgen
turtle.penup()
turtle.goto(-200,-200)
turtle.pensize(3)
turtle.color("red","yellow")
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    turtle.forward(80)
    turtle.left(72)
turtle.end_fill()
#daire
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.color("blue","brown")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.done()