#200
para = int(input("kaç para çekeceksiniz:"))
ikiyuz = para // 200#1
print(ikiyuz,"adet 200 ₺")#2
#100
para = para - ikiyuz*200#3
yuz = para // 100
print(yuz," adet 100 ₺")
#50
para = para -yuz*100
elli = para//50
print(elli,"adet 50 ₺")
#20
para = para - elli*50
yirmi = para // 200
print(yirmi,"adet 20 ₺")
#10
para = para - yirmi*20
on = para//10
print(on,"adet 10₺")