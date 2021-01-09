import turtle
import time
turtle.shape("turtle")
icRenk=input("renk gir:")
disRenk="blue"
kalem=4
r=int(input("yarıçap gir:"))
turtle.pensize(kalem)
turtle.color(disRenk,icRenk)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
# turtle.forward(200)
# turtle.begin_fill()
# turtle.circle(r)
# turtle.end_fill()


turtle.done()