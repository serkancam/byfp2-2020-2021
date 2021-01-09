import turtle as t
import random

t.shape("turtle")
t.Screen().setup(600, 600)

t.pensize(60)

for i in range(5):
    k = random.uniform(0, 1)  # 0 ile 1 arasında bir ondalıklı sayı tut
    y = random.uniform(0, 1)
    m = random.uniform(0, 1)
    # demet(tuple)  (k,y,m) her renge 0.0    .... 1.0 değerler verebiliyorum
    renk = (k, y, m)
    t.color(renk)
    t.forward(60)
    t.right(72)

t.done()
