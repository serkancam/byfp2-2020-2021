import turtle as t 
t.Screen().setup(600,400)
t.shape("turtle")
# çözüm buraya yapılacak
for i in range(3):
    for k in range(6):
        t.forward(50)
        t.right(60)
    #ileri atla
    t.penup()
    t.forward(100)
    t.pendown()    



t.done()