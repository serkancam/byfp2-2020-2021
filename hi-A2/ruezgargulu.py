import turtle as t 

t.Screen().setup(600,600)
t.pensize(4)
for i in range(6):
    for k in range(3):
        t.color("maroon")
        t.forward(100)
        t.right(60)
        t.color("blue")
        t.forward(50)
        t.right(60)
    t.right(60)

    


t.done()