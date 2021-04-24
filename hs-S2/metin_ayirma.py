giris = input("isimleri araya boşluk koyarak giriniz:")
print(giris.split(" "))
isimler = giris.split(" ")
print("eleman sayısı=",len(isimler))
for isim in isimler:
    print(isim)
giris2 = input("boy değerlerini araya virgül koyarak giriniz:")
boylar = giris2.split(",")
toplam_boy=0
for boy in boylar:
    print(boy)
    toplam_boy = toplam_boy + float(boy)
print("boy ortalması=",toplam_boy/len(boylar))
