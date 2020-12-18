import turtle
turtle.shape("turtle")

while True:
    yon = input("yon gir:")

    if yon == "a":
        turtle.left(90)
        turtle.forward(100)
    elif yon == "d":
        turtle.right(90)
        turtle.forward(100)
    elif yon == "s":
        turtle.left(180)
        turtle.forward(100)
    elif yon == "w":
        turtle.forward(100)
    else:
        break
#turtle.forward(100)

turtle.done()
