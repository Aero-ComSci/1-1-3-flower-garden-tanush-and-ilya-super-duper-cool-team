#HI ILYA KONICHIWA IM YOUR BIGGEST FAN ILYA BILYA REPLY TO ME ILYA KAWAII PLSSSSS

import turtle as t
#lily!!!
t.speed(35)
#petals
def lily():
  
  def petal():
      t.color("purple")
      t.begin_fill()
      t.circle(45, 60)  
      t.left(120)
      t.circle(45, 60)  
      t.left(120)
      t.end_fill()
  
  # Draw the petals
  for idk in range(6):
      petal()
      t.right(60)  
  
  #draw the thingies in the middle
  t.pencolor("darkgreen")
  t.pensize(5)
  startpos = t.position()
  t.circle(-15,70)
  t.penup()
  t.setposition(startpos)
  t.pendown()
  t.left(90)
  t.circle(-15,70)
  t.setposition(startpos)
  # Draw the stem
  t.setheading(270)
  t.penup()
  t.forward(40)
  t.pensize(5)
  t.pendown()
  t.forward(50)
  #leaf
  t.fillcolor('lightgreen')
  t.begin_fill()
  t.left(70)
  t.circle(50,43)
  t.left(120) 	
  t.circle(50,43)
  #stem pt 2
  t.setheading(270)
  t.forward(70)
  t.end_fill()
  
  
  wn = t.Screen()
  wn.mainloop()
