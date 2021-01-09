a = int(input("a kenar uzunluğunu giriniz:"))
b = int(input("b kenar uzunluğunu giriniz:"))
c = int(input("c kenar uzunluğunu giriniz:"))

# a+b>c ve a+c>b ve b+c>a kuralına uymalı

print(a+b>c)
print(a+c>b)
print(b+c>a)

print("bu sayılardan üçgen olur mu?",a+b>c and a+c>b and b+c>a)

if a+b>c and a+c>b and b+c>a:
    print(a,b,c,"uznluklarından üçgen olur")
    print("o zaman üçgen alanını hesaplayabiliriz")
else:
    print(a,b,c,"uzunluklarından üçgen olmaz.")
    print("alan da hesaplanamaz.")
