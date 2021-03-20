# abc
# acb
# bca
# bac
# cba
# cab
a = input("3 basamaklı bir sayı giriniz:")
b = input("3 basamaklı bir sayı giriniz:")
c = input("3 basamaklı bir sayı giriniz:")
ebs =int(a+b+c) # + operatörü işleme girenler string ise onları birleşitirir.
if int(a+c+b)>ebs:
    ebs = int(a+c+b)
if int(b+c+a)>ebs:
    ebs = int(b+c+a)
if int(b+a+c)>ebs:
    ebs = int(b+a+c)
if int(c+b+a)>ebs:
    ebs=int(c+b+a)
if int(c+a+b)>ebs:
    ebs=int(c+a+b)
print(ebs)