import turtle as t
import time

t.shape("turtle")#arrow, turtle, circle, triangle
t.Screen().setup(600,480)
t.penup()
time.sleep(2)
t.goto(-50,-50)
t.pendown()
for hasan in range(4):
    t.forward(100)
    t.left(90)
#farklı yol
# t.penup()
# t.goto(50,50)
# t.left(180)
# t.color("red")
# t.pendown()
# for huseyin in range(4):
#     t.forward(100)
#     t.left(90)
t.penup()
t.goto(-50,240)
t.pendown()
for ali in range(4):
    t.forward(100)
    t.right(90)
t.done()

