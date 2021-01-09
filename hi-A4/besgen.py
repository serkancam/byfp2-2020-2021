import turtle
import random
turtle.shape("turtle")
turtle.Screen().setup(600,600)

#https://studio.code.org/s/coursef-2017/stage/7/puzzle/6 bağlantısındaki sahnenin çözümü

turtle.pensize(5)
for i in range(5):
    kirmizi=random.uniform(0,1)#renk ağırlıkları 0....1 arasındaki ondalıklı sayılarla olur
    yesil = random.uniform(0,1)
    mavi =random.uniform(0,1)
    renk = (kirmizi,yesil,mavi)#tuple
    turtle.color(renk)
    turtle.forward(60)
    turtle.right(72)

turtle.done()