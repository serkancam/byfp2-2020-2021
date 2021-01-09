a=int(input("a uzunluğunu gir:"))
b=int(input("b uzunluğunu gir:"))
c=int(input("c uzunluğunu gir:"))
print(a+b>c)
print(a+c>b)
print(b+c>a)
#and (ve): koşullardan biri bile false ise sonuç false. Hepsi True ise sonu true olur
print("sonuç",a+b>c and a+c>b and b+c>a)

if a+b>c and a+c>b and b+c>a:
    print("bu değerlerden üçgen olur.")
    print("üçgen alanı hesapla.")
    print("daha neler neler yapabilirim.")
else:
    print("bu değerlerden üçgen olmaz.")
    print("alanda hesaplanmmaz")
    print("buadan sonra ne yapacağına karar ver")

pirnt("karar bitti.")

