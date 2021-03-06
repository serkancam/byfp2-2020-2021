import turtle 

ta = int(input("Kaç tel var?:"))
tu = 0
for i in range(ta):
    t = int(input(str(i+1)+". tel uzunluğunu gir:"))
    tu= tu+t

kalan = tu%4
cevre = tu-kalan
print("çevre=",cevre,"metre")
print("kalan tel=",kalan,"metre")
for i in range(4):
    turtle.forward(cevre/4)
    turtle.right(90)
turtle.done()