import turtle as t 

t.shape("turtle")
t.Screen().setup(600,600)
y=200
x=-200
t.penup()
t.goto(x,y)
t.pendown()
for i in range(64):
    if i%16==0:
        t.penup()
        t.goto(x,y)
        y=y-100
        t.pendown()
    elif i%4==0:        
        t.forward(100)
    t.forward(100)
    t.right(90)
t.done()