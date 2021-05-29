dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read()
dosya.close()
donem_ortalamasi=0.0
not_adet=0
for satir in metin.split("\n"):
    ders_adi=satir.split(":")[0].strip()
    notlar = satir.split(":")[1].strip().split(" ")
    ortalama=0.0
    for nt in notlar:
        ortalama = ortalama + float(nt)
        donem_ortalamasi=donem_ortalamasi+float(nt)
        not_adet=not_adet+1
    ortalama = ortalama / len(notlar)
    print(ders_adi,"ortalamasi=",round(ortalama,2))
donem_ortalamasi = donem_ortalamasi/not_adet
print("dönem ortalaması=",round(donem_ortalamasi,2))




"""
Matematik ortalaması= 75
Türkçe ortalaması=87.5
Sosyal bilgiler ortalaması=95
Fen bilimleri ortalaması=97.5
İngilizce ortalaması=82.5
Dönem ortalaması=?
"""