import turtle
import random

turtle.shape("turtle")
turtle.Screen().setup(600, 600)
# çözüm buraya olacak
turtle.pensize(5)
for _ in range(5):
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    renk = (r, g, b)#demet(tuple)
    turtle.color(renk)
    turtle.forward(60)
    turtle.right(72)
    
turtle.done()
