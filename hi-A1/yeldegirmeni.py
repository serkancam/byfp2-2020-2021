import turtle as t 

t.Screen().setup(600,600)
#çözüm buraya yazılacak
for i in range(9):
    t.forward(50)
    for k in range(3):
        t.forward(50)
        t.right(120)
    t.backward(50)
    t.right(40)


t.done()


