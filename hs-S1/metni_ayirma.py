giris = input("isimleri araya boşluk ekleyerek yazınız:")
print(giris.split(" "))
isimler = giris.split(" ")
giris2 = input("kişilerin boylarını araya virgül koyarak giriniz:")
boylar = giris2.split(",")

toplam_boy=0
for boy in boylar:
    print(boy)
    # buraya toplam_boy dğişkenine boy değerlerini ekleyecek kodu yazınız
    toplam_boy += float(boy)  #toplam_boy = toplam_boy + boy


print("boy ortalaması=",toplam_boy/len(boylar))