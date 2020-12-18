import turtle as t  # alias

t.shape("turtle")
t.Screen().setup(600, 600)
t.Screen().bgcolor("light green")

metin = input("yaz:")
t.penup()
t.goto(0, 250)


metin=metin.upper()
metin=metin.lower()
metin=metin.strip()
metin=metin.replace("u","i")
# metin=metin.replace("h","")

isimler = metin.split(",")



t.write(metin, font=("Arial", 16, "underline"))

iks,ye=t.position()
t.color("red")#

for isim in isimler:
    ye=ye-50
    t.goto(iks,ye)
    t.write(isim,font=("comic sans",16,"italic"))#t.write(isim)



t.done()
