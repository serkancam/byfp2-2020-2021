import turtle
turtle.shape("turtle")

turtle.color("red","red")
turtle.begin_fill()

turtle.forward(300)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.end_fill()

turtle.color("white","white")
turtle.penup()
turtle.goto(180,50)
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    turtle.forward(60)
    turtle.left(144)
turtle.end_fill()

#hilal
turtle.penup()
turtle.goto(60,20)
turtle.pendown()
turtle.color("white","white")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.color("red","red")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.hideturtle()
turtle.done()