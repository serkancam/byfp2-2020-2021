dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read() 
dosya.close()
# print(metin)
satirlar = metin.split("\n")#\n= enter
# print(satirlar)
for satir in satirlar:
    bilgi=satir.split(":")
    ders_adi=bilgi[0]
    notlar=bilgi[1].strip().split(" ")
    print("ders adi=",ders_adi)
    print("notlar=",notlar)
    ort=0
    for nt in notlar:
        ort=ort+float(nt)
    ort=ort/len(notlar)
    print(ders_adi,"dersinin ortaamasi=",ort)
    print("*"*20)
