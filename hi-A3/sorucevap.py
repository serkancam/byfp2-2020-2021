sorular=["3*3 kaçtır? :","27/9 kaçtır? :","3-2 kaçtır? :","30+5 kaçtır? :"]#10000 soru olsun
sorular.append("üçgen iç açıları toplamı nedir?")
dcevaplar=[9,3,1,35,180]
ocevaplar=[]

for soru in sorular:
    #print(soru)
    cevap =int(  input(soru)   )
    ocevaplar.append(cevap)

soruBasiPuan= 100/len(sorular)
dcs=0

for i in range(len(sorular)):
    if dcevaplar[i]==ocevaplar[i]:
        dcs=dcs+1

print("puanınız:",dcs*soruBasiPuan)