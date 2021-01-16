import turtle as t

t.Screen().setup(600, 600)
# https://studio.code.org/s/course4/stage/10/puzzle/2

for adim in range(50, 101, 10):  # 50 60 70 80 90 100
    for i in range(3):  # 0 1 2
        t.forward(adim)
        t.left(120)

t.done()
