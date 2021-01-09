import turtle
import time
turtle.shape("turtle")#fonksyion/method

ic=input("renk gir:")
dis="blue"
#r=int(input("r gir:"))
r=input("r gir:")
r=int(r)
kb=4

turtle.color(dis,ic)
turtle.begin_fill()
turtle.pensize(kb)
turtle.circle(r)
turtle.end_fill()
turtle.forward(30)
time.sleep(2)
turtle.color(dis,ic)
turtle.begin_fill()
turtle.pensize(kb)
turtle.circle(r)
turtle.end_fill()
turtle.forward(30)

turtle.done()