import turtle as t
t.Screen().setup(600,600)
t.shape("turtle")

for i in range(3):
    for k in range(6):
        t.forward(50)
        t.right(60)
    #ileri nasıl atlanır
    t.penup()
    t.forward(100)
    t.pendown()
t.done()
