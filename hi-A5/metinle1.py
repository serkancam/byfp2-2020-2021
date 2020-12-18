import turtle as t

t.shape("turtle")
t.Screen().setup(600,600)
t.Screen().bgcolor("light green")

metin=input("yaz:")
t.penup()
t.goto(0,250)
metin=metin.upper()
metin=metin.lower()
metin=metin.strip()
# metin = metin.replace("a","e")
# metin=metin.replace("i","")
#metin=metin.replace("-","\n")
metin=metin.replace("-",",")
isimler=metin.split(",")

t.write(metin,font=("Arial",20,"underline"))

iks,ye=t.position()

for isim in isimler:
    ye=ye-50
    t.goto(iks,ye)
    t.write(isim)


t.hideturtle()
t.done()