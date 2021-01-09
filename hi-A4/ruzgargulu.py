import turtle as t 

t.Screen().setup(600)
#çözüm buraya
t.pensize(4)
for i in range(6):#0-1-2-3-4-5-
    for r in range(3):#0-1-2-
        t.color("purple")
        t.forward(100)
        t.right(60)
        t.color("blue")
        t.forward(50)
        t.right(60)
    t.right(60)
t.done()