import turtle as t 

t.shape("turtle")
t.Screen().setup(600,500)
t.color("red")
t.forward(300)
t.backward(600)
t.goto(0,0)
t.left(90)
t.color("green")
t.forward(250)
t.backward(500)
t.goto(0,0)
t.penup()
t.goto(-50,-50)
t.color("black")
t.pendown()
print(t.heading())
for i in range(4):
    t.forward(100)
    t.right(90)
    print(t.heading())

t.penup()
t.goto(-50,150)
t.pendown()
for hasan in range(4):
    t.forward(100)
    t.right(90)

t.done()