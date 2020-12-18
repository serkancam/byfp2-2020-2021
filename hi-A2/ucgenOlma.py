a = int(input("a kenar uzunluğunu giriniz:"))
b = int(input("b kenar uzunluğunu giriniz:"))
c = int(input("c  kenar uzunluğunu giriniz:"))

if a+b>c and a+c>b and  b+c>a: 
    print("üçgen olur")
else:
    print("üçgen olamaz")