# dosyalara bağlan
dosyaSorular = open("sorular.txt","r",encoding = "utf-8")
dosyaCevaplar = open("cevaplar.txt","r",encoding="utf-8")
# dosya içeriklerini  programa aktar
sorular = dosyaSorular.readlines()
cevaplar = dosyaCevaplar.readlines()
# dosyaları kapat
dosyaCevaplar.close()
dosyaSorular.close()
# soruları sor ve cevapları al
ocevaplar = []
for soru in sorular:
    cevap = input(soru)
    ocevaplar.append(cevap)
# değerlendir ve sonucu yazdır
sorubasiPuan = 100 / len(sorular)
dcs = 0
for i in range(len(sorular)):
    if cevaplar[i].rstrip("\n").strip().lower()==ocevaplar[i].strip().lower():
        dcs+=1
print("puanınız:",dcs*sorubasiPuan)
