import turtle as t 

t.pensize(5)

for uzunluk in range(10,101,10):
    t.left(90)
    t.forward(uzunluk)
    t.backward(uzunluk)
    t.right(90)
    t.penup()
    t.forward(10)
    t.pendown()

# #10 luk
# t.left(90)
# t.forward(10)
# t.backward(10)
# t.right(90)
# t.penup()
# t.forward(10)
# t.pendown()
# # 20 lik
# t.left(90)
# t.forward(20)
# t.backward(20)
# t.right(90)
# t.penup()
# t.forward(10)
# # 30 lik
# t.left(90)
# t.forward(30)
# t.backward(30)
# t.right(90)
# t.penup()
# t.forward(10)
# t.pendown()

t.done()