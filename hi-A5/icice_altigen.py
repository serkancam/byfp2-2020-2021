import turtle as t  

for i in range(3):
    for k in range(6):
        t.forward(50)
        t.right(60)
    # ileri atla
    t.penup()
    t.forward(100)
    t.pendown()

t.done()