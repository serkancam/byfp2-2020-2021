import turtle
import random
turtle.shape("turtle")
turtle.Screen().setup(600,600)
# yandaki kodu buraya yazınız
turtle.pensize(5)
for i in range(5):
    # r = random.uniform(0,1)
    # g = random.uniform(0,1)
    # b = random.uniform(0,1)
    # renk = (r,g,b)
    # turtle.color(renk)# 
    turtle.color(   (   random.uniform(0,1),  random.uniform(0,1),  random.uniform(0,1)      )      )
    turtle.forward(60)
    turtle.right(72)


# print(turtle.color())
turtle.done()