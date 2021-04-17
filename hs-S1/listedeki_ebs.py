#listedeki_ebs.py
l=[7,12,20,5,2,1,30]#100.000 adet sayı
print(l)
sayi = int(input("sayı giriniz:"))
l.append(sayi)
sayi = int(input("sayı giriniz:"))
l.append(sayi)
print(l)
for s in l:
    print(s)

ebs = l[0]
# if l[1]>ebs:
#     ebs=l[1]
# if l[2]>ebs:
#     ebs=l[2]
for s in l:
    if s>ebs:
        ebs=s
print("en büyük sayı:",ebs)
# ortalama,ortanca
toplam = 0
for s in l:
    toplam = toplam+s
ortalama = toplam/len(l)
print("ortalama:",ortalama)

# listede ortalama değere en yakın sayıyı bulunuz.
