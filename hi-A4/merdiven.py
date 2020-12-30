# https://studio.code.org/s/coursef-2017/stage/7/puzzle/7
# sahnesini 400*400 oiksellik arkaplan rengi mor olacak şekilde python a uyarlayınız.

import turtle as t  #t takma adı verdim


t.Screen().setup(400,400)
t.bgcolor((.2,.6,.8))#
t.pensize(20)
for i in range(3):
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)

t.done()

