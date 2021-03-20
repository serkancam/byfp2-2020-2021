import turtle

turtle.Screen().setup(600, 600)

adet = int(input("Kaç adet telin var?:"))

toplam = 0
for i in range(adet):
    uz = int(input(str(i+1)+". telin uzunluğunu giriniz:"))
    toplam = toplam+uz

kalan = toplam % 4
cevre = toplam - kalan
print("Karenin çevresi:", cevre, "metred")
print("Kalan tel", kalan, "metre")
for k in range(4):
    turtle.forward(cevre/4)
    turtle.right(90)

turtle.done()
