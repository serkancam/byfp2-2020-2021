import turtle as t  

t.Screen().setup(610,610)
# https://studio.code.org/s/course4/stage/10/puzzle/2

for counter in range(50,101,10):
    for i in range(3):
        t.forward(counter)
        t.left(120)


t.done()
