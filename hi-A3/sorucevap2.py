#ilk önce dosyalara erişim yapılır
dosyaS = open("sorular.txt","r",encoding="utf-8")
dosyaC = open("cevaplar.txt","r",encoding="utf-8")

# dosyalardan verileri al
sorular = dosyaS.readlines()
cevaplar = dosyaC.readlines()
# dosyaları kapat
dosyaC.close()
dosyaS.close()
# soruları sor
ocevaplar=[]
for soru in sorular:
    cevap = input(soru)
    ocevaplar.append(cevap)

dcs=0
soruBasiPuan=100/len(sorular)
# puanlama yap
for i in range(len(sorular)):
    if cevaplar[i].rstrip("\n").strip().lower()==ocevaplar[i].strip().lower():
        dcs+=1

print("puanınız:",dcs*soruBasiPuan)