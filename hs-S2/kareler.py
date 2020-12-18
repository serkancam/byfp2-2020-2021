import turtle as t 

t.shape("turtle")
t.Screen().setup(600,600)
x=-100
y=100
t.penup()
t.goto(x,y)
t.pendown()

for c in range(4):
    for i in range(4):
        for k in range(4):
            t.forward(50)
            t.right(90)
        t.forward(50)
    t.penup()
    y=y-50
    t.goto(x,y)
    t.pendown()
# for i in range(4):
#     for k in range(4):
#         t.forward(50)
#         t.right(90)
#     t.forward(50)

t.done()