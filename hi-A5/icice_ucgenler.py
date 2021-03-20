import turtle as t 
t.Screen().setup(600,600)

for counter in range(50,102,10):
    for i in range(3):#0 1 2 
        t.forward(counter)
        t.left(120)


t.done()