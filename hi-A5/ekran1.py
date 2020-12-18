import turtle

turtle.shape("turtle")

turtle.Screen().setup(640,427)
turtle.Screen().bgcolor("light green")
turtle.Screen().bgpic("bayrak.gif")
turtle.penup()
turtle.goto(0,180)
#turtle.color("white")
turtle.write("ISTIKLAL MARSI",align="center",font=("Arial",20,"bold"))
misra1="Korkma, sönmez bu şafaklarda yüzen al sancak;"
turtle.goto(0,150)
turtle.color("white")
turtle.write(misra1,align="center",font=("gabriola",14,"italic"))


turtle.hideturtle()
turtle.done()