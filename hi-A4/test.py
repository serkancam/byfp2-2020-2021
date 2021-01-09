import json
def turkceisimdenEposta(isim):    
    isim.replace('ğ',"g") 
    isim.replace('Ğ',"g")
    isim.replace('ı',"i")
    isim.replace('İ',"i")
    isim.replace('ö',"o")
    isim.replace('Ö',"o")
    isim.replace('ü',"u")
    isim.replace('Ü',"u")
    isim.replace('ş',"s")
    isim.replace('Ş',"s")
    isim.replace('ç',"c")
    isim.replace('Ç',"c")
    return isim


d = open("isimler.txt","r",encoding="ISO-8859-9")
e = open("epostalar.txt","w+")
satirlar = d.readlines()
d.close()
isimler=[]
for i in satirlar:
    isim = i.lower().strip("\n").strip().replace(" ",".")
    isim=turkceisimdenEposta(isim)
    isimler.append(isim)
   


print(isimler)