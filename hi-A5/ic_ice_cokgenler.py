import turtle as t 

t.Screen().setup(600,750)

for counter in range(3,11,1):
    for i in range(counter):
        t.forward(100)
        t.right(360/counter)
# t.write("merhaba",font=("Arial",50,"b
# old"))
t.done()