import turtle
import time

turtle.shape("turtle")

icRenk=input("renk gir:")
disRenk=input("çizgi rengi:")
kalem=int(input("kalem kalınlığı:"))
r=int(input("yarıçap:"))

turtle.color(disRenk,icRenk)
turtle.begin_fill()
turtle.pensize(kalem)
time.sleep(5)

turtle.circle(r)
turtle.end_fill()

turtle.done()