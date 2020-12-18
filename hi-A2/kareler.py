import turtle as t 

t.Screen().setup(600,600)
t.shape("turtle")

t.penup()
t.goto(-200,200)
t.down()
for i in range(4):
    t.forward(100)
    t.right(90)

t.forward(100)
for i in range(4):
    t.forward(100)
    t.right(90)
t.forward(100)
for i in range(4):
    t.forward(100)
    t.right(90)

t.forward(100)
for i in range(4):
    t.forward(100)
    t.right(90)
t.penup()
t.goto(-200,100)
t.done()

