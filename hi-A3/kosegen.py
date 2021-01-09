import turtle as t 
t.shape("turtle")
t.Screen().setup(600,600)
#serkan yöntemi
t.goto(300,300)
t.goto(0,0)
t.goto(-300,300)
t.goto(0,0)
t.goto(-300,-300)
t.goto(0,0)
t.goto(300,-300)
t.goto(0,0)
# ayşe yöntemi
t.pensize(3)
t.color("red")
t.left(45)
for k in range(4):
    t.forward(424)
    t.backward(424)
    t.left(90)
t.right(45)
#sol alt kırmızı
t.begin_fill()
t.goto(-300,300)
t.goto(-300,-300)
t.goto(300,-300)
t.goto(0,0)
t.end_fill()
t.done()