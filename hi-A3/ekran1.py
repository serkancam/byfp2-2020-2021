import turtle
turtle.shape("turtle")

turtle.Screen().bgcolor("green")
turtle.Screen().setup(800,800)
turtle.Screen().bgpic("bayrak.gif")
turtle.color("blue")
turtle.penup()
turtle.goto(0,350)
turtle.write("İSTİKLÂL MARŞI",align="right",font=("Arial",20,"bold"))
turtle.goto(0,320)
m1 = "Korkma, sönmez bu şafaklarda yüzen al sancak;"
turtle.write(m1,align="left",font=("Arial",18,"normal"))


turtle.done()