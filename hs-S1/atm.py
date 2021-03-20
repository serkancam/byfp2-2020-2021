# 200
para = int(input("para miktarını giriniz:"))
ikiyuz = para // 200
print(ikiyuz,"adet 200 ₺")
#100
para=para-ikiyuz*200
yuz = para // 100
print(yuz,"adet 100 ₺")#altgr+t
#50
para = para-yuz*100
elli = para // 50
print(elli,"adet 50 ₺")
# 20
para = para - elli*50
yirmi=para//20
print(yirmi,"adet 20 ₺")
# 10
para = para-yirmi*20
on = para // 10
print(on,"adet 10₺")