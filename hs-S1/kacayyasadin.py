import datetime
simdi= datetime.datetime.now()
syil=simdi.year
say=simdi.month
dyil = int(input("Hangi yıl doğdun:"))
day = int(input("Kaçıncı ay doğdun:")) 
yay = (2020-dyil)*12+(11-day)
print(yay,"aylıksın.")