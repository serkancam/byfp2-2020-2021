import turtle as t 

t.shape("turtle")
t.Screen().setup(600,600)
t.goto(300,300)
t.goto(-300,300)
t.goto(300,-300)
t.goto(-300,-300)
t.goto(0,0)
#sol alt kırmızı
t.color("green","red")
t.begin_fill()
t.goto(-300,300)
t.goto(-300,-300)
t.goto(300,-300)
t.goto(0,0)
t.end_fill()
#sağ üst yeşil

t.done()