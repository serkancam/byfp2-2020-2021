import turtle

turtle.shape("turtle")


turtle.Screen().bgcolor("green")
turtle.Screen().setup(600,400)
#turtle.Screen().bgpic("bg.gif")

turtle.forward(120)
turtle.left(90)
turtle.screensize(20)
turtle.write("Merhaba",font=("Arial",28,"bold"))

turtle.hideturtle()
turtle.done()