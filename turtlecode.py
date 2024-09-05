import turtle as t
#sunflower!!!
t.speed(0.2)
#position setup
t.speed(100)
t.penup()
t.goto((-180,-150))
t.left(90)
t.pensize(8)
t.pendown()
right=30
#stem and leaf
def sunflower():
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
    t.goto((-180,25))
    t.pencolor("saddlebrown")
    #flower petals
    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.pencolor("yellow2")
    t.setheading(0)
    t.pensize(25)
    t.penup()
    t.goto((-180,50))
    t.pendown()
    for fpetal in range(0, 360, 40):
        t.penup()
        t.setheading(fpetal)  
        t.forward(40)  
        t.dot(15 * 2, "yellow")
        t.backward(40)
        
        
    t.done()


    wn = t.Screen()
    wn.mainloop()

