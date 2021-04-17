veri = input("Sınıftaki öğrencilerin boylarını araya virgül koyarak giriniz:")
print(veri)  # 1.74,1.86,1.75,1.65,1.55
boylar = veri.split(",")
print(boylar)
i = 0
toplam_boy = 0.0
for boy in boylar:
    i += 1
    print(i, ". öğrencinin boyu=", boy)
    toplam_boy = toplam_boy + float(boy)

print("toplam boy=",toplam_boy)