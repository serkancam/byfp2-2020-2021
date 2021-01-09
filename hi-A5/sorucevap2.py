# dosyalara bağlantı kur
dosyas = open(file="sorular.txt",mode="r",encoding="utf-8")
dosyac = open(file="cevaplar.txt",mode="r",encoding="utf-8")
# dosyalardan verileri al
sorular = dosyas.readlines()
cevaplar = dosyac.readlines()
# dosyaları kapat
dosyas.close()
dosyac.close()
# soruları sorup cevapları kaydet
ocevaplar=[]
for soru in sorular:
    cevap = input(soru)
    ocevaplar.append(cevap)
# cevpları karşılaştır ve puan hesapla
soruBasiPuan = 100 / len(sorular)
dcs = 0
for i in range(len(sorular)):
    if cevaplar[i].rstrip("\n").strip().lower() == ocevaplar[i].strip().lower():
        dcs+=1

puan = dcs*soruBasiPuan
# puanı ekrana yazdır
print("puanınız:",puan)