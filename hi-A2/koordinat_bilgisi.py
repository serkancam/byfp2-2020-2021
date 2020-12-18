import turtle as t 
import time

t.shape("turtle")
t.Screen().setup(600,600)
t.Screen().bgcolor("light green")
#iş burada 
t.penup()
t.goto(-50,-50)
print(t.heading())
t.pendown()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.goto(50,200)
t.left(90)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)
t.done()