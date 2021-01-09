dosyaS = open("sorular.txt","r", encoding="utf-8")
dosyaC = open("cevaplar.txt","r", encoding="utf-8")

sorular = dosyaS.readlines()
cevaplar = dosyaC.readlines()

dosyaS.close()
dosyaC.close()

ocevaplar=[]
for soru in sorular:
    cevap = input(soru) 
    ocevaplar.append(cevap)

dcs=0
soruBasiPuan=100/len(sorular)

for i in range(len(sorular)):
    if cevaplar[i].lower().rstrip('\n')==ocevaplar[i].lower():
        dcs = dcs+1


print("puan:",dcs*soruBasiPuan)