dosya = open(file="notlar.txt",mode="r",encoding="utf-8")
metin=dosya.read()
dosya.close()
# print(metin)
# print(metin.split("\n"))
satirlar=metin.split("\n")

"""
Matematik ortalaması 75
fen bilgisi ortalaması  85
sosyal bilgiler ortalaması  92.5
Türkçe  82.5
"""