s1 = "3*3 kaçtır? :"
s2 = "27/9 kaçtır? :"
s3 = "üçgen iç açıları toplamı nedir?:"

sorular = [s1, s2, s3, "27-5 kaçtır? :"]
sorular.append("iki katının 10 eksiği 8 olan sayı kaçtır?:")

dcevaplar = [9, 3, 180, 22]
dcevaplar.append(9)
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
# if dcevaplar[0] == ocevaplar[0]:
#    dcs = dcs+1
# if dcevaplar[1] == ocevaplar[1]:
#    dcs = dcs+1
# if dcevaplar[2] == ocevaplar[2]:
#    dcs = dcs+1
# if dcevaplar[3] == ocevaplar[3]:
#    dcs = dcs+1
