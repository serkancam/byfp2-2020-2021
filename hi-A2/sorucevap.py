sorular=["3+3 kaçtır?","3*3 kaçtır?","9*8 kaçtır?","27/9 kaçtır?","3/3 kaçtır?"]
# print(len(sorular))
# print(sorular[1])
dcevaplar=[6,9,72,3,1]
ocevaplar=[]
for soru in sorular:
    cevap=int(input(soru))
    ocevaplar.append(cevap)

#bu hafta
sorubasipuan=100/len(sorular)
dcs=0
i=0
while i<len(sorular):
    if dcevaplar[i]==ocevaplar[i]:
        dcs=dcs+1
    i=i+1

puan=dcs*sorubasipuan
print(puan)

