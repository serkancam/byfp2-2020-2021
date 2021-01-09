import turtle as t 

t.Screen().setup(600,600)
#çözüm
t.pensize(5)
for d in range(6):
    for g in range(3):
        t.color("purple")
        t.forward(100)
        t.right(60)
        t.color("blue")
        t.forward(50)
        t.right(60)
    t.right(60)
t.done()