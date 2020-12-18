#########kareler_kisayol.py###############
import turtle as t 
t.shape("turtle")
t.Screen().setup(600,600)

t.penup()
x=-200
y=200
t.goto(x,y)
t.pendown()
for a in range(4):
    for b in range(4):
        for c in range(4):
            t.forward(100)
            t.right(90)
        t.forward(100)
    t.penup()
    y=y-100
    t.goto(x,y)
    t.pendown()



t.done()