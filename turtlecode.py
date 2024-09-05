import turtle as trtl
t = trtl.Turtle()
#sunflower!!!
t.speed(0.2)
#position setup
t.speed(100)
t.penup()
t.goto((0,-150))
t.left(90)
t.pensize(8)
t.pendown()

#stem and leaf
t.pencolor("darkgreen")
t.forward(125)
#leaf
t.fillcolor('lightgreen')
t.begin_fill()
t.left(70)
t.circle(100,43)
t.left(120) 	
t.circle(100,43)
t.end_fill()
t.goto((0,25))
t.pencolor("saddlebrown")
#flower petals
t.fillcolor("saddlebrown")
t.begin_fill()
t.circle(30)
t.end_fill()
t.pencolor("yellow2")


wn = trtl.Screen()
wn.mainloop()

