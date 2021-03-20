import  turtle as t
# https://studio.code.org/s/course4/stage/10/puzzle/5

t.Screen().setup(650,650)
for uzunluk in range(15,301,15):
    t.forward(uzunluk)
    t.left(90)


t.done()