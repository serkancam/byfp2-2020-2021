# listedeki_ebs.py
g = []
l = [2, 3, 5, 7, 1, 8, 10, 22]
sayi = int(input("sayı gir:"))
l.append(sayi)
sayi = int(input("sayı gir:"))
l.append(sayi)
print(l)
for s in l:
    print(s)
ebs = l[0]  # ilk başta listenin ilk elemanının en büyük kabul ediyorum
for s in l:
    if s > ebs:
        ebs = s
print("en büyük sayı:", ebs)

toplam = 0
for s in l:
    toplam = toplam+s
ortalama = toplam/len(l)
print("ortalama=",ortalama)

# bu sayı listesindeki ortalama değere en yakın sayıyı bulunuz.

# if l[0]>ebs:
#     ebs=l[0]
# if l[1]>ebs:
#     ebs=l[1]
# if l[2]>ebs:
#     ebs=l[2]
# if l[3]>ebs:
#     ebs=l[3]
