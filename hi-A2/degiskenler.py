import turtle
import time

turtle.shape("turtle")
icRenk = input("iç renk belirle:")
r = int(input("çap gir:"))
disRenk = "blue"
kalem=4
turtle.color(disRenk,icRenk)
turtle.pensize(kalem)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

for _ in range(4):
    turtle.forward(80)
    turtle.left(90)
    time.sleep(1)

turtle.done()