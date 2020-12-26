import turtle as t
import random

t.shape("turtle")
t.Screen().setup(600, 600)
# çözüm buradan itibaren
t.pensize(60)

for i in range(5):
    k = random.uniform(0,1)
    y = random.uniform(0,1)
    m = random.uniform(0,1)
    renk = (k, y, m)  # demet(tuple)   (kırmızı,yeşil,mavi)
    t.color(renk)
    t.forward(60)
    t.right(72)

t.done()
