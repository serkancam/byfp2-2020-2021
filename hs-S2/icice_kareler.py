import turtle as t 
t.Screen().setup(650,650)
t.speed(0)
# https://studio.code.org/s/course4/stage/10/puzzle/4
for counter in range(15,301,15):
    for kez in range(4):
        t.forward(counter)
        t.left(90)


t.done()
