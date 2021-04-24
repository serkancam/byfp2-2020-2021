dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read()
dosya.close()
# print(metin)
for satir in metin.split("\n"):
    # print("ders adı:",satir)
    ders_adi=satir.split(":")[0].strip()
    notlar = satir.split(":")[1].strip().split(" ")
    #ders_adi,notlar=satir.split(":")
    ortalama=0.0
    for nt in notlar:
        ortalama = ortalama + float(nt)
    ortalama = ortalama / len(notlar)
    print(ders_adi,"ortalamasi=",ortalama)
    # print(ders_adi)
    # print(notlar)
    # print("*"*20)


"""
Matematik ortalaması= 75
Türkçe ortalaması=87.5
Sosyal bilgiler ortalaması=95
Fen bilimleri ortalaması=97.5
İngilizce ortalaması=82.5
Dönem ortalaması=85
"""