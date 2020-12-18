s1 = "3*3 kaçtır? :"
s2 = "27/9 kaçtır? :"
s3 = "25-4 kaçtır? :"

sorular = [s1, s2, s3]
sorular.append("33+7 kaçtır? :")

sorular.append("üçgen iç açıları toplamı nedir?")
dcevaplar = [9, 3, 21, 40, 180]  # soruların doğru cevapları
kcevaplar = []  # kullanıcının cevaplar/bir boş liste

soruBasiPuan = 100 / len(sorular)
dcs = 0

for soru in sorular:
    cevap = int( input(soru) )
    kcevaplar.append(cevap)

for i in range(len(sorular)):
    if dcevaplar[i] == kcevaplar[i]:
        dcs += 1     #dcs = dcs + 1

print("puan:",dcs*soruBasiPuan)
#cevaplar kontrol edilecek

# ctrl tuşuna basılı iken ö tuşuna basıyoruz
# if dcevaplar[0]==kcevaplar[0]:
#     dcs = dcs+1
# if dcevaplar[1] == kcevaplar[1]:
#     dcs = dcs + 1
# if dcevaplar[2] == kcevaplar[2]:
#     dcs = dcs + 1
# if dcevaplar[3] == kcevaplar[3]:
#     dcs = dcs + 1
# if dcevaplar[4] == kcevaplar[4]:
#     dcs = dcs + 1