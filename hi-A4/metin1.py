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
# metin=metin.replace("u","i")
metin=metin.replace("h","")

isimler=metin.split(",")
t.write(metin,font=("Arial",20,"underline"))

x,y=t.position()#0,250
for isim in isimler:
    y=y-30
    t.goto(x,y)
    t.write(isim)


t.hideturtle()
t.done()