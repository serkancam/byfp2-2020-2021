a = int(   input("a  uzunluğunu giriniz:")  )
b = int( input("b  uzunluğunu giriniz:") )
c = int( input("c uzunluğunu giriniz:") ) 

# print(a+b>c)
# print(a+c>b)
# print(b+c>a)

print("sonuç",a+b>c and a+c>b and b+c>a)

if a+b>c and a+c>b and b+c>a:
    print("bu değerlerden üçgen olur")
    print("alan hesaplanır.")
    print("açıları bul")
else:
    print("bu değerlerden üçgen olmaz.")
    print("alan hesaplanamaz.")
    print("açılar bulunamaz.")

print("program bitt.")