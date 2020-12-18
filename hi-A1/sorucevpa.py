s1 = "10+1 kaçtır?"
s2 = "7+3 kaçır?"
s3 = "üçgen içi açıları toplamı kaçtır?"
s4 = "pi sayısı genelde yuvarlanarak kaç alınır?"
# 1000 soru için daha 996 satır kod ve 996 farklı değişken
# c1 = input(s1)
# c2 = input(s2)
# c3 = input(s3)
# c4 = input(s4)
# her cevap için 996 değişken ve satır
sorular = ["10+1 kaçtır?","7+3 kaçtır?","üçgenin iç açıları toplamı kaçtır?"]
sorular.append(s4)
#print(sorular[0])
#print(sorular[1])
#print(sorular[2])
#print(sorular[3])
sorular.append("8*6 kaçtır?")
sorular.append("3+2 nin 3 katı kaçtır?")
sorular.append("2 katının 10 eksiği 8 olan sayı kaçtır")
sorular.append("dik açı kaç derecedir?")
sorular.append("en küçük asal sayı kaçtır?")
sorular.append("3 basamaklı raklamları birbirinden farklı en küçük doğal sayı kaçtır?")
dcevaplar = [11,10,180,3,48,15,9,90,2,102]
ogr_cevaplar=[]
for soru in sorular:
   c=int(input(soru))
   ogr_cevaplar.append(c)

soruBasiPuan = 100/len(sorular) 
dcs = 0

for i in range(len(sorular)):
   if ogr_cevaplar[i]==dcevaplar[i]:
      dcs+=1#dcs=dcs+1
print("puan:",dcs*soruBasiPuan)

# if ogr_cevaplar[0]==dcevaplar[0]:
#    dcs=dcs+1
# if ogr_cevaplar[1]==dcevaplar[1]:
#    dcs=dcs+1
# if ogr_cevaplar[2]==dcevaplar[2]:
#    dcs=dcs+1
# if ogr_cevaplar[3]==dcevaplar[3]:
#    dcs=dcs+1
# if ogr_cevaplar[4]==dcevaplar[4]:
#    dcs=dcs+1