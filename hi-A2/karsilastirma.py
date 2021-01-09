import turtle
turtle.shape("turtle")
turtle.Screen().setup(600,400)

while True:
    yon = input("yön gir:")
    if yon == "a":
        turtle.left(90)
    elif yon=="d":
        turtle.right(90)
    elif yon=="s":
        turtle.left(180)
    elif yon=="w":
        pass
    else:
        continue

    turtle.forward(100) 

turtle.done()