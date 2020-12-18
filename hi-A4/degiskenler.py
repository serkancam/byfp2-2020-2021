import turtle
import time




#turtle.speed(1)
turtle.shape("turtle")#fonksiyon/method paramtere alır
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
#değişkenler
icRenk=input("iç renk bilgisi:")
disRenk="blue"
r=int(input("yarı çap gir:"))
turtle.color(disRenk,icRenk)
kalem=4
turtle.pensize(kalem)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()




turtle.done()#ben kapatmadan kapanma