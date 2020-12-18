import turtle
import time

turtle.shape("turtle")
# time.sleep(1)
# turtle.forward(50)
# time.sleep(1)
# turtle.left(90)
# turtle.forward(50)
# time.sleep(1)
# turtle.left(90)
# turtle.forward(50)
# time.sleep(1)
# turtle.left(90)
# turtle.forward(50)
# time.sleep(1)
# turtle.left(90)

for i in range(4):
    turtle.forward(50)
    time.sleep(1)
    turtle.left(90)

turtle.up()
turtle.forward(100)
turtle.down()
turtle.speed(0)
for i in range(360):
    turtle.forward(1)
    turtle.left(1)

turtle.done()