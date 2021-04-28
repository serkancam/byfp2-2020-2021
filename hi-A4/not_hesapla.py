dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read() 
dosya.close()
satirlar = metin.split("\n")#\n= enter
donem_notu = 0
not_sayisi = 0
for satir in satirlar:
    ders_adi=satir.split(":")[0].strip()
    notlar=satir.split(":")[1].strip().split(" ")
    ort=0
    for nt in notlar:
        ort=ort+float(nt)
        donem_notu = donem_notu +float(nt)
        not_sayisi+=1
    ort=ort/len(notlar)
    print(ders_adi,"=",ort)
print("Dönem sonu=",donem_notu/not_sayisi)
# print(donem_notu)
# print(not_sayisi)