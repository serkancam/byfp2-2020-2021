dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read()
dosya.close()
satirlar = metin.split("\n")
for satir in satirlar:
    ders_adi=satir.split(":")[0].strip()
    notlar=satir.split(":")[1].strip().split(" ")
    ort=0.0
    for nt in notlar:
        ort = ort + int(nt)
    ort = ort/len(notlar)
    print(ders_adi,"=",round(ort,2))










"""
Matematik ortalaması= 75
Türkçe ortalaması=87.5
Sosyal bilgiler ortalaması=95
Fen bilimleri ortalaması=97.5
İngilizce ortalaması=82.5
"""