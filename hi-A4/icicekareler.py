import turtle as t 

t.Screen().setup(600,600)
# https://studio.code.org/s/course4/stage/10/puzzle/4
t.penup()
t.goto(-100,-100)
t.pendown()
t.pensize(4)
t.speed(0)
kareSayisi=0
for adim in range(15,301,15):
    for i in range(4):
        t.forward(adim)
        t.left(90)
    kareSayisi+=1

print(kareSayisi)

t.done()