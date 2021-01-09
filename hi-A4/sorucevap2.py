dosyaS = open("sorular.txt","r",encoding="utf-8")
dosyaC = open("cevaplar.txt","r",encoding="utf-8")

sorular = dosyaS.readlines()
cevaplar = dosyaC.readlines()
sorular[-1]+="\n"
dosyaS.close()
dosyaC.close()

# soruları sor
ocevaplar = []
for soru in sorular:
    cevap = input(soru)
    ocevaplar.append(cevap)

dcs = 0
soruBasiPuan = 100 / len(sorular)
#puanlama / sınav sonucu bul

for i in range(len(sorular)):
    if cevaplar[i].strip().lower().rstrip("\n") == ocevaplar[i].strip().lower():
        dcs = dcs + 1

print("puanınız:",dcs*soruBasiPuan)