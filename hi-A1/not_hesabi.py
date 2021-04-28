dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin=dosya.read()
dosya.close()
satirlar=metin.split("\n")
for ders in satirlar:
    ders_adi=ders.split(":")[0].strip()
    notlar= ders.split(":")[1].strip().split(" ")
    ort=0
    for nt in notlar:
        ort=ort+float(nt)
    ort = ort/len(notlar)
    print(ders_adi,"=",ort)

"""
matematik = 80.0      
fen bilgisi = 85.0    
sosyal bilgiler = 92.5
Türkçe = 87.5
İngilizce = 87.5
dönem sonu= 85
"""