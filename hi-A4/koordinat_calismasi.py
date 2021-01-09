import turtle as t

t.shape("turtle")
t.Screen().setup(640,480)

#buraya çözüm yapıalacak 
t.penup()
t.goto(-50,-50)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(50,140)
t.pendown()
for h in range(4):
    t.left(90)
    t.forward(100)



t.done()
