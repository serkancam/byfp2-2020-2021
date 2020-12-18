import turtle

def sol():
    turtle.left(90)
    turtle.forward(100)

def geri():
    turtle.left(180)
    turtle.forward(100)
def temizle():
    turtle.clear()

turtle.shape("turtle")
turtle.Screen().setup(500,500)


turtle.onkey(sol,"a")
turtle.onkey(geri,"s")
turtle.onkey(temizle,"Down")
turtle.listen()

turtle.done()