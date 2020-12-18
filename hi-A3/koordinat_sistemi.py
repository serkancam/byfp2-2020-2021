import turtle as t 

t.shape("turtle")
t.Screen().setup(600,600)
t.penup()
t.goto(-50,-50)
t.pendown()

for k in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-50,300)
t.pendown()
for k in range(4):
    t.forward(100)
    t.right(90)



t.done()