# matametik ortlamanız 75
# fen bilgisi ortalamanız 92.5
dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin = dosya.read()
dosya.close()
# print(metin)
for satir in metin.split("\n"):
    print("ders adı:",satir)