# def topla(liste):
#     toplam=0
#     if isinstance(liste,(int,float)):
#         return liste
#     for i in liste:
#         if isinstance(liste,dict):
#             toplam+=topla(liste.get(i))
#         elif isinstance(i,(list,tuple,dict,set)):
#             toplam+=topla(i)
#         elif isinstance(i,(int,float)):
#             toplam+=i
#     return toplam
# if __name__=="__main__":
#     t1=["12","ali",1,2.0,10]
#     t2=(1,2,(10,3,{3,6,3}))
#     t3={"a":1,"b":[t1,t2]}
#     t4=(1,2,[3,(4,5,{7,8}),{"a":12,"b":[3,8,[12]]}])
#     print(topla(t1))
#     print(topla(t2))
#     print(topla(t3))
#     print(topla(t4))

def topla(liste):
    for x in range(1):
        print(sum(liste))


t1 = [ 1, 2.0, 10,[1,2]]
t2 = (1, 2, (10, 3, {3, 6, 3}))
t3 = {"a": 1, "b": [t1, t2]}
t4 = (1, 2, [3, (4, 5, {7, 8}), {"a": 12, "b": [3, 8, [12]]}])
print (sum (t1)) #13.0
print (sum (t2)) #25
# print (sum (t3)) #39
# print (sum (t4)) #65