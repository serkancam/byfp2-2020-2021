import turtle as t 
import random
t.shape("turtle")
t.Screen().setup(600,600)
#çözüm buraya yazılacak
t.pensize(60)
for i in range(5):
    k = random.uniform(0,1) # verilen iki sayı arasında rastgele ondalıklı sayılar tutar
    y = random.uniform(0,1)
    m = random.uniform(0,1)
    renk = (k,y,m) # demet(tuple) 3 buda 3 tane sayıyı bir arada tutuyor.
    t.color(renk)
    t.forward(60)
    t.right(72)
t.done()
