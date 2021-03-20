import turtle as t 

t.Screen().setup(650,650)
# https://studio.code.org/s/course4/stage/10/puzzle/4
t.speed(0)

for adim in range(15,301,15):
    for kenar in range(4):
        t.forward(adim)
        t.left(90)



t.done()
