dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read()
dosya.close()
print(metin)

satirlar = metin.split("\n")

for satir in satirlar:
    print("satır:",satir)


"""
Matematik ortalaması= 75
Türkçe ortalaması=87.5
Sosyal bilgiler ortalaması=95
Fen bilimleri ortalaması=97.5
İngilizce ortalaması=82.5

"""