import turtle

def sol():#fonskiyon(işlev)
    turtle.left(90)
    turtle.forward(100)

def geri():
    turtle.left(180)
    turtle.forward(100)

def temizle():
    turtle.clear()

def sag():
    turtle.right(90)
    turtle.forward(100)

#def definition--> taımlama
def ileri():
    turtle.forward(100)

turtle.shape("turtle")
turtle.Screen().setup(600,600)
#olay güdümlü progralama(event)
turtle.onkey(sol,"a")
turtle.onkey(geri,"s")
turtle.onkey(sag,"d")
turtle.onkey(ileri,"w")
turtle.onkey(temizle,"Down")
turtle.listen()



turtle.done()