import turtle
# tel adeti--->ta
# tel uzunluğuna -->tu
# toplam tel uzunluğun< --> tt
ta = int(input("Kaç adet tel var?: "))
tt = 0
for i in range(ta):
    tu = int(input(str(i+1) + ". tel uzunluğunu giriniz:"))
    tt = tt+tu

kalan = tt % 4
cevre = tt-kalan
print("cevre:",cevre,"metre")
print(kalan,"metre tel kalmıştır.")
