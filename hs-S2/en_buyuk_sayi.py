# abc
# acb
# bac
# bca
# cab
# cba
# liste=['a',367,458,201] 62 karakteri yazıp 
a=input("3 basamaklı sayı giriniz:") 
b=input("3 basamaklı sayı giriniz:") 
c=input("3 basamaklı sayı giriniz:") 
ebs=int(a+b+c)

if int(a+c+b)>ebs:
    ebs = int(a+c+b)
if int(b+a+c)>ebs:
    ebs=int(b+a+c)
if int(b+c+a)>ebs:
    ebs = int(b+c+a)
if int(c+a+b)>ebs:
    ebs=int(c+a+b)
if int(c+b+a)>ebs:
    ebs = int(c+b+a)

print(ebs)



