giris = input("isimleri araya boşluk koyarak yazınız:")
print(giris.split(" "))
isimler = giris.split(" ")
giris2 = input("boy değelerini araya virgül koyarak giriniz:")
boylar=giris2.split(",")

toplam_boy=0
for boy in boylar:
    print(boy)
    toplam_boy = toplam_boy + float(boy)

print("boy ortalaması=",toplam_boy/len(boylar))