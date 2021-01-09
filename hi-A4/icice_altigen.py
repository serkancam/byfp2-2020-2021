import turtle as t 

t.Screen().setup(600,600)
t.pensize(4)
t.penup()
t.goto(-250,250)
t.pendown()

for i in range(3):
    for k in range(6):
        t.forward(50)
        t.right(60)
    t.penup()
    t.forward(100)
    t.pendown()


t.done()