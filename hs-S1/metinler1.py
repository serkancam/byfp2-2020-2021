import turtle as t  # alias - takma ad
# import random as r
# import time as tm

t.Screen().setup(600, 600)
t.Screen().bgcolor("light green")
t.shape("turtle")

metin = input("yaz:")
metin = metin.upper()
metin = metin.lower()
metin = metin.strip()#lstrip rstrip
metin=metin.replace("u","i")
t.penup()
t.goto(0, 250)
t.write(metin, font=("Arial", 16, "underline"))

t.done()
