#soru ve cevapları dosyalardan al
dosyaS = open("sorular.txt","r",encoding="utf-8")
dosyaC = open("cevaplar.txt","r",encoding="utf-8")

#dosyalardan satırları okuyup değişkenlere aktardım
sorular = dosyaS.readlines()
cevaplar = dosyaC.readlines()
#dosya bağlantılarını kapatıyorum
dosyaC.close()
dosyaS.close()
#soruları sor cevapları bir listeye al
ogr_cevaplar = []
for soru in sorular:
    cevap = input(soru)
    ogr_cevaplar.append(cevap)

soruBasiPuan = 100 /len(sorular)
dcs = 0

for i in range(len(sorular)):
    if ogr_cevaplar[i].strip().lower()==cevaplar[i].rstrip("\n").strip().lower():
        dcs+=1

print("puanınız:",dcs*soruBasiPuan)
