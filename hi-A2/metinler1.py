import turtle as t

t.shape("turtle")
t.Screen().setup(600,600)
t.Screen().bgcolor("green")

metin = input("adını yaz:")
metin=metin.upper()
metin=metin.strip()
metin=metin.lower()
# metin=metin.replace("a","i")
metin=metin.split(",")
t.penup()
t.goto(0,250)
x,y=t.position()
for isim in metin:
    t.write(isim,font=("Arial",30,"underline"))
    y=y-50
    t.goto(x,y)
t.hideturtle()
t.done()
