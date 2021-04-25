giris = input("isimleri araya boşluk koyarak yazınız:")
print(giris.split(" "))
isimler = giris.split(" ")
for isim in isimler:
    print(isim)

giris2="1.74,1.58,1.70,1.68"
boylar = giris2.split(",")
toplam_boy=0
for boy in boylar:
    # print(boy)
    toplam_boy = toplam_boy + float(boy)

print("Sınıfın boy ortalaması=",toplam_boy/len(boylar))



