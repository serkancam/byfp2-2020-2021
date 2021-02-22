import turtle
turtle.Screen().setup(600,600)
turtle.pensize(4)
turtle.penup()
# dış dörtgen
turtle.goto(-200,100)
turtle.pendown()
for i in range(2):
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
#sol çember
turtle.penup()
turtle.goto(-130,-40)
turtle.pendown()
turtle.circle(40)
#iç dörtgen
turtle.penup()
turtle.forward(70)
turtle.pendown()
for i in range(2):
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
#sağ çember
turtle.penup()
turtle.forward(190)
turtle.pendown()
turtle.circle(40)
turtle.done()