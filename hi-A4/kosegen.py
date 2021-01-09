import turtle as t 

t.shape("turtle")
t.Screen().setup(600,600)
#çözüm buradan sonraya
t.goto(300,300)
t.goto(-300,300)
t.goto(300,-300)
t.goto(-300,-300)
t.goto(0,0)
#sol alt kırmızı boyama
t.goto(-300,300)
t.color("green","red")#t.color("red")
t.begin_fill()
t.goto(-300,-300)
t.goto(300,-300)
t.goto(-300,300)
t.end_fill()
t.goto(0,0)
#sağ üst yeşil boyama






t.done()