import turtle
import time

turtle.shape("turtle")


icRenk=input("renk gir:")
disRenk=input("çizgi rengi gir:")
r=int(input("r gir:"))
k=4


turtle.color(disRenk,icRenk)
turtle.pensize(k)
turtle.begin_fill()
turtle.circle(r)#hata çünkü r değişkeninin değeri bir tam sayı olmalı
turtle.end_fill()

turtle.forward(30)

turtle.color(disRenk,icRenk)
turtle.pensize(k)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

turtle.forward(30)
turtle.color(disRenk,icRenk)
turtle.pensize(k)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

turtle.forward(30)
turtle.color(disRenk,icRenk)
turtle.pensize(k)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

turtle.forward(30)
turtle.color(disRenk,icRenk)
turtle.pensize(k)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

turtle.forward(30)
turtle.done()