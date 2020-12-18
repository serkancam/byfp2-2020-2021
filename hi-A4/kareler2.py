import turtle as t 

t.shape("turtle")
t.Screen().setup(800,600)

x=-200
y=200
for i in range(64):
    if i%16==0:
        t.penup()
        t.goto(x,y)
        t.pendown()
        y=y-100
    elif i%4==0:
        t.forward(100)
    t.forward(100)
    t.right(90)

t.done()

