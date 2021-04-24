dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read()
dosya.close()
satirlar = metin.split("\n") 
for satir in satirlar:
    ders_adi=satir.split(":")[0].strip()
    notlar= satir.split(":")[1].strip().split(" ")
    ort=0
    for nt in notlar:
        ort=ort+float(nt)
    ort=ort/len(notlar)
    print(ders_adi,"dersi ortalması=",ort)
    
