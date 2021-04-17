giris = input("isimleri araya boşluk bırakarak yazınız:")
#birce bengusu elis doğan serkan
giris2=input("boy bilgilerini araya virgül kouarak giriniz:")
#1.65,1.58,1.56,1.60,1.74
print(giris.split(" "))
isimler=giris.split(" ")
for isim in isimler:
    print(isim)

boylar = giris2.split(",")
print(boylar)
toplam_boy=0
for boy in boylar:
    toplam_boy=toplam_boy + float(boy)

print("sınıfın boy ortalaması=",toplam_boy/len(boylar))