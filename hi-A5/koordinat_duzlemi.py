import turtle as t 


t.shape("turtle")
t.Screen().setup(600,600)
t.delay(5)
t.penup()
t.goto(-50,-50)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(50,300)
t.right(90)
t.down()
for k in range(4):
    t.forward(100)
    t.right(90)
#en alt kare size çalışma
t.done()