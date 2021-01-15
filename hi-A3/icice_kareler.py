import turtle as t 

t.Screen().setup(800,800)
t.speed(0)
for adim in range(15,301,15):
    for kez in range(4):
        t.forward(adim)
        t.left(90)


t.done()