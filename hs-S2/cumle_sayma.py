dosya = open(file="metin.txt",mode="r",encoding="utf-8")
metin = dosya.read()#karakter dizisi
dosya.close()
# print(metin)
# print(len(metin))
cs=0
for krk in metin:
    if krk=="?" or krk=="." or krk=="!":
        cs = cs+1# cs+=1
print("Metinde",cs,"adet cümle vardır.")
hs=0
for krk in metin:
    if krk in "euıoüaiöEUIOÜAİÖ":
        hs+=1

print("Metinde",hs,"adet hece vardır.")  