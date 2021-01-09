import turtle
turtle.shape("turtle")#turtle parametre
turtle.penup()#fonksiyon/method
turtle.goto(-200,-200)#-200 -200
turtle.pendown()
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

turtle.penup()
turtle.goto(-20,-140)
turtle.pendown()
turtle.color("white","white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()
#hilal
turtle.penup()
turtle.goto(-140,-180)
turtle.pendown()
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.color("red","red")
turtle.forward(20)
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.done()