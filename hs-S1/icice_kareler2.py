import turtle as t 

t.Screen().setup(650,650)
# https://studio.code.org/s/course4/stage/10/puzzle/5
t.speed(0)
t.pensize(4)
for adim in range(15,301,15):
    t.forward(adim)
    t.left(90)


t.done()