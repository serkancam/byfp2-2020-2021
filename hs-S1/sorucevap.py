s1 = "3*3 kaçtır? :"
s2 = "27/9 kaçtır? :"
s3 = "7+8 kaçtır? :"

sorular = [s1, s2, s3]
sorular.append("30-25 kaçtır? :")
sorular.append("ügen iç açıları toplamı kaçtır? :")
dcevaplar = [9, 3, 15, 5,180]
ocevaplar = []

for soru in sorular:
    cevap = int(input(soru))
    ocevaplar.append(cevap)

soruBasiPuan = 100/len(sorular)
dcs = 0

for i in range(len(sorular)):
    if dcevaplar[i] == ocevaplar[i]:
        dcs = dcs+1

print("puan:", dcs*soruBasiPuan)



