a = int(input("a kenar uzunluğunu giriniz:"))
b = int(input("b kenar uzunluğunu giriniz:"))
c = int(input("c kenar uzunluğunu giriniz:"))

print(a+b>c)#True
print(a+c>b)#True
print(b+c>a)#True

print("sonuç:",a+b>c and a+c>b and b+c>a )

if a+b>c and a+c>b and c+b>a:
    print(a,b,c,"bunlardan uçgen olur.")
    
else:
    print(a,b,c,"bunlardan üçgen olmaz")