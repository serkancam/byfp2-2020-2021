import turtle


turtle.shape("turtle")
turtle.Screen().setup(640,427)
turtle.Screen().bgcolor("blue")
turtle.Screen().bgpic("bayrak.gif")
turtle.penup()
turtle.goto(0,180)
turtle.color("white")

turtle.write("İSTİKLÂL MARŞI", align="center",font=("Arial",20,"bold"))
ms1 = "Korkma, sönmez bu şafaklarda yüzen al sancak;"
turtle.goto(0,150)
turtle.write(ms1,align="center",font=("Arial",16,"italic"))




turtle.done()