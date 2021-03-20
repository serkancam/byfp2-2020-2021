import turtle
# ts --> tel sayısı
# tu --> toplam uzunluk
# gd --> o anda girilen telin uzunluğu
# kalan --> kalan tel uzunluğu
# cevre--> en büyük oluşacak karenini çevresi
ts = int(input("Tel sayısını gir:"))
tu = 0
for a in range(ts):
    gd = int(input("tel uzunluğunuı giriniz:"))
    tu = gd+tu

kalan = tu % 4
cevre =  tu - kalan
print("karenin çevresi",cevre,"metredir.")

print(kalan,"metre tel kalşmıştır.")
for q in range(4):
    turtle.forward(cevre/4)
    turtle.right(90)
turtle.done()
