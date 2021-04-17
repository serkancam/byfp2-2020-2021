dosya = open(file="metin.txt",mode="r",encoding="utf-8")
metin = dosya.read()
dosya.close()
# print(metin)
cumles=0
for krk in metin:
    # print(krk)
    if krk=="." or krk=="?" or krk=="!":
        cumles=cumles+1#cumles+=1
print("Metinde",cumles,"adet cümle var.")
heces=0
for krk in metin:
    if krk in "EUIOÜAİÖeuıoüaiö" :
      heces+=1
print("Metinde",heces,"adet hece vardır.")