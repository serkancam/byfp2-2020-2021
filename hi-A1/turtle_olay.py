import turtle

def sol():
    turtle.left(90)
    turtle.forward(100)
def sag():
    turtle.right(90)
    turtle.forward(100)

def geri():
    turtle.left(180)
    turtle.forward(100)

def ileri():
    turtle.forward(100)

turtle.shape("turtle")
turtle.Screen().setup(600,600)

turtle.onkey(sol,"a")
turtle.onkey(sol,"u")# bu satırı yazma
turtle.onkey(sag,"d")
turtle.onkey(geri,"s")
turtle.onkey(ileri,"w")
turtle.onkey(turtle.clear,"space")
turtle.listen()


turtle.done()
