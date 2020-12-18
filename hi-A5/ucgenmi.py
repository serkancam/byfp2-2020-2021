a = int(input("a kenar uzunluğunu giriniz:")) 
b = int(input("b kenar uzunluğunu giriniz:")) 
c = int(input("c kenar uzunluğunu giriniz:")) 

print(a+b>c)
print(a+c>b)
print(b+c>a)

print("bunlardan üçgen olur mu? :",a+b>c and b+c>a and a+c>b)

if a+b>c and b+c>a and a+c>b:
    print(a,b,c,"uznluklarından üçgen olur.")
else:
    print(a,b,c,"uznluklarından üçgen olmaz.")
