#dosyalara bağlantı kur
sd = open(file="sorular.txt",mode="r",encoding="utf-8")
cd = open(file="cevaplar.txt",mode="r",encoding="utf-8")
#dosyalardaki verileri programa aktar
sorular = sd.readlines()
cevaplar = cd.readlines() 
#dosya bağlantılarını kapa
sd.close()
cd.close()
#soruları sor cevapları al
ocevaplar=[]
for soru in sorular:
    cevap = input(soru)
    ocevaplar.append(cevap)
#cevapları değerlendir puan hesapla
dcs=0
soruBasiPuan=100/len(sorular)
for i in range(len(sorular)):
    if cevaplar[i].rstrip("\n").strip().lower()==ocevaplar[i].strip().lower():
        dcs+=1
#puanı ekrana yazdır.
print("puanınız:",dcs*soruBasiPuan)
