import turtle
# ta --> tel adeti
# tt --> toplam tel uzunluğu
# tu --> o anda girilen tel uzunluğu
ta = int(input("Kaç adet tel var?: "))
tt = 0
for i in range(ta):
    tu = int(input("tel uzunluğunu giriniz: "))
    tt = tt+tu
print("toplam uzunluk:", tt)

kalan = tt % 4
cevre = tt-kalan
print("karenin çevresi",cevre,"metredir.")
print("geriye",kalan,"metre tel kalmıştır.")
