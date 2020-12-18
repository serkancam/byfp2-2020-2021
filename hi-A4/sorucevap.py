s1 = "3*3 kaçtır?"
s2 = "iki katının 5 ekiği 5 olan sayı kaçtır?"
s3 = "27-9 işleminin sonucu kaçtır?"
# 997 satır kod ve değişken lazım
# s1000="bi soru"
sorular = ["3*3 kaçtır", "iki katının 5 eksiği 5 olan sayı kaçtır?",
           "27-9 işleminin sonucu kaçtır", "1+1 kaçtır?", "üçgen iç açıları toplamı kaçtır"]

dcevaplar = [9, 5, 18, 2, 180]
print(dcevaplar[0])
ocevaplar = []  # elemansız bir liste

for soru in sorular:
    cevap =int( input(soru) )
    ocevaplar.append(cevap)

soruBasiPuan = 100/len(sorular)
dcs = 0
print("sorular bitti")  # yazmayın
for i in range(len(sorular)):
    if dcevaplar[i] == ocevaplar[i]:
        dcs = dcs+1

print("puanınız:", dcs * soruBasiPuan)
