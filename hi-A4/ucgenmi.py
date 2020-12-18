a = int( input("a kenar uzunluğunu giriniz:") )
b = int( input("b kenar uzunluğunu giriniz:") )
c = int( input("c kenar uzunluğunu giriniz:") )

# a+b>c 
# b+c>a
# a+c>b

sonuc = a+b>c and b+c>a and a+c>b

if a+b>c and b+c>a and a+c>b:
    print("üçgen olur")
else:
    print("üçgen olamaz")