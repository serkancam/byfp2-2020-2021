para = int(input("kaç para "))

for banknot in [200,100,50,20,10]:
    adet = para // banknot
    print(adet,"adet",banknot,"₺")
    para = para-adet*banknot


    