import turtle
# ts --> tel sayısı
# tu --> toplam uzunluk
# gd --> o anda girilen telin uzunluğu
# kalan --> kalan tel uzunluğu
# cevre--> en büyük oluşacak karenini çevresi
ts = int(input("Tel sayısını giriniz:"))
tu = 0
for p in range(ts):
    gd = int(input("Tek uzunluğunu girinz:"))
    tu = tu + gd
kalan = tu % 4
cevre = tu - kalan
# kenar = int(tu/4)#x.yy--> x
# cevre = kenar*4
# kalan = tu-cevre
print("kare çevresi", cevre,"metredi")
print(kalan,"metre tel artmıştır.")
for f in range(4):
    turtle.forward(cevre/4)
    turtle.right(90)