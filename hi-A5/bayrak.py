import turtle
turtle.shape("turtle")
#dikdörtgen
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
#yıldız
turtle.penup()
turtle.goto(180,50)
turtle.pendown()
turtle.color("white","white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(60)
    turtle.left(144)
turtle.end_fill()

#hilal

turtle.penup()#fonksiyon/method parantez içine yazdıklarımız parametre
turtle.goto(100,20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.color("red")
turtle.forward(20)
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()











turtle.hideturtle()
turtle.done()