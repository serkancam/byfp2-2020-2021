import turtle

turtle.shape("turtle")

turtle.Screen().setup(640,427)
turtle.Screen().bgcolor("light blue")
turtle.Screen().bgpic("bayrak.gif")#gif olmalı
turtle.penup()
turtle.goto(0,180)
turtle.write("İSİLÂL MARŞI",align="center",font=("Arial",20,"bold"))
turtle.color("white")
turtle.goto(0,150)
ms1="Korkma, sönmez bu şafaklarda yüzen alsancak;"
turtle.write(ms1,align="center",font=("Arial",16,"italic"))

turtle.hideturtle()
turtle.done()