# kişinin doğduğu tarih bilgisini alıp kaç ay yaşadığını bulalım
# kişiden doğduğu gün ay yıl bilgisi alıp bunu hesaplayalım

# dyil = int(input("doğduğun yılı gir:"))
d_yil = input("doğduğun yılı gir:")
d_yil= int(d_yil)
d_ay = int(input("kaçıncı ayda doğdun:"))
yf= 2020-d_yil
af=11-d_ay

y_as = yf*12+af
print(y_as,"ay yaşadınız")
