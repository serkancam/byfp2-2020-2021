import turtle

turtle.Screen().setup(600, 600)
# tel sayısına ts
ts = int(input("Elinde kaç adet tel var?:"))
# toplam tel uzunluğuma tu
tu = 0
for i in range(1, ts+1):
    t = int(input(str(i) + ". tel uzunluğu: ")) # tu =tu+ int(input(str(i) + ". tel uzunluğu: "))
    tu = tu+t
print("toplam tel uzunluğu:", tu, "metredir")
kalan_tel = tu % 4
bir_kenar = (tu-kalan_tel)/4
kare_cevre =int(( bir_kenar*4))
print("en büyük kare çevresi:",kare_cevre,"metre")
print("kalan tel",kalan_tel,"metre")

for t in range(4):
    turtle.forward(bir_kenar)
    turtle.right(90)

turtle.done()
