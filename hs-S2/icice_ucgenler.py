import turtle as t 

t.Screen().setup(600,600)
# https://studio.code.org/s/course4/stage/10/puzzle/2

for degisken in range(50,101,10):
    for i in range(3):
        t.forward(degisken)
        t.left(120)


t.done()