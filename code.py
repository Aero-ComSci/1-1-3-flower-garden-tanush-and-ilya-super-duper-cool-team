

import turtle as t
flowers = {"rose", "lily", "sunflower", "daisy", "tulip","roses", "lilies", "sunflowers", "daisies", "tulips"}
# from TEST import roser
# from sunflower3 import sunflower
x = input("Pick some flowers (separate by spaces): ").lower()  
y = x.split() 
com2 = len(y) 
com = 0
current_x = -t.window_width() // 2 + 50

def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))
def tulip():
    t.speed(0)
    global current_x
    t.speed(100)
    t.penup()
    t.goto((current_x, -150)) 
    t.setheading(90) 
    t.pendown()
#tulip!!!

#stem
    
    t.setheading(270)
    t.penup()
    t.forward(50)
    t.pencolor("darkgreen")
    t.left(180)
    t.pendown()
    t.pensize(5)
    t.forward(100)
    #leaf
    t.fillcolor('lightgreen')
    t.begin_fill()
    t.left(70)
    t.circle(50,43)
    t.left(120) 	
    t.circle(50,43)
    t.end_fill()
    #petals
    t.fillcolor("orange")
    t.left(82)
    t.forward(75)
    t.pencolor("orange")
    t.right(90)
    t.penup()
    t.pendown()
    t.begin_fill()
    t.circle(50,-90)
    t.left(40)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.setheading(0)
    t.forward(30)
    t.right(70)
    t.forward(30)
    t.setheading(0)
    t.left(75)
    t.forward(30)
    t.setheading(95)
    t.circle(63,-60)
    t.end_fill()
    current_x += 150  

def sunflower1():
    global current_x
    t.speed(100)
    t.penup()
    t.goto((current_x, -150)) 
    t.setheading(90) 
    t.pensize(5)
    t.pendown()

    
    t.pencolor("darkgreen")
    t.forward(125)
    t.fillcolor('lightgreen')
    t.begin_fill()
    t.left(70)
    t.circle(100, 43)
    t.left(120)
    t.circle(100, 43)
    t.end_fill()

 
    t.goto((current_x, 25)) 
    t.pendown()
    t.pencolor("saddlebrown")
    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

   
    t.pencolor("yellow2")
    t.setheading(0) 
    t.pensize(25)
    t.penup()
    t.goto((current_x, 50))  
    t.pendown()
    for fpetal in range(0, 360, 40):
        t.penup()
        t.setheading(fpetal)  
        t.forward(40)
        t.dot(15 * 2, "yellow")
        t.backward(40)

   
    current_x += 150  

def rose():
    global current_x

    s = 0.2 
    t.pensize(2)
    t.color("red")
    t.pencolor("black")
    t.fillcolor("red")
    t.speed(100)
    t.penup()
    t.setheading(360)
    t.goto(current_x, 450 * s)  
    t.pendown()

    t.begin_fill()
    t.circle(100 * s, 30) 
    DegreeCurve(60, 25 * s)  
    t.circle(100 * s, 30)  
    DegreeCurve(4, 50 * s)  
    t.circle(100 * s, 50)  
    DegreeCurve(50, 25 * s)  
    t.circle(175 * s, 65)  
    DegreeCurve(40, 35 * s)  
    t.circle(75 * s, 50)  
    DegreeCurve(20, 25 * s, -1)  
    t.circle(200 * s, 60)  
    DegreeCurve(18, 25 * s)  
    t.fd(125 * s) 
    t.right(150)
    t.circle(-250 * s, 12) 
    t.left(140)
    t.circle(275 * s, 110)  
    t.left(27)
    t.circle(325 * s, 100)  
    t.left(130)
    t.circle(-150 * s, 20)  
    t.right(123)
    t.circle(110 * s, 57)
    t.end_fill()

    t.left(120)
    t.fd(140 * s)  
    t.left(115)
    t.circle(150 * s, 33) 
    t.left(180)
    t.circle(-150 * s, 33)  
    DegreeCurve(70, 112.5 * s, -1)  
    t.circle(175 * s, 104)  
    t.left(90)
    t.circle(100 * s, 105) 
    t.circle(-250 * s, 63)  
    t.penup()
    
    t.goto(current_x +16, 10* s)  
    t.pendown()
    t.color("darkgreen")
    t.pensize(5)
    t.setheading(270)
    t.fd(150)
    t.setheading(90)
    t.fd(35)
    t.fillcolor('lightgreen')
    t.begin_fill()
    t.circle(70, 70)
    t.left(110)
    t.circle(70, 70)
    t.end_fill()

    current_x += 100  
    
def lily():
    global current_x  
    t.penup()
    t.goto(current_x, 0) 
    t.pendown()

    for idk in range(6):
        t.color("purple")
        t.begin_fill()
        t.circle(45, 60)
        t.left(120)
        t.circle(45, 60)
        t.left(120)
        t.end_fill()
        t.right(60)

    t.pencolor("darkgreen")
    t.pensize(5)
    startpos = t.position() 
    t.circle(-15, 70)
    t.penup()
    t.setposition(startpos)
    t.pendown()
    t.left(90)
    t.circle(-15, 70)
    t.setposition(startpos)
    #stem
    t.setheading(270)
    t.penup()
    t.forward(40)
    t.pensize(5)
    t.pendown()
    t.forward(50)

    #Leaf
    t.fillcolor('lightgreen')
    t.begin_fill()
    t.left(70)
    t.circle(50, 43)
    t.left(120)
    t.circle(50, 43)
    
    
    t.setheading(270)
    t.forward(70)
    t.end_fill()


    current_x += 150 
def daisy():
    global current_x 
    t.speed(0)
    t.pensize(1)
    t.penup()
    t.goto(current_x, 90)
    t.pendown()
    for _ in range(10): 
        t.color("lightblue")
        t.begin_fill()
        t.circle(50, 60)  
        t.left(120)
        t.circle(50, 60) 
        t.left(120)
        t.end_fill()
        t.left(36)  
    t.color("green")
    t.setheading(270)
    t.forward(170)
    t.backward(170) 

    current_x += 80

   
    
flower_functions = {
    "tulip": tulip,
    "tulips": tulip,
    "sunflower": sunflower1,
    "sunflowers": sunflower1,
    "rose": rose,
    "roses": rose,
    "lily": lily,
    "lilies": lily,
    "daisy": daisy,
    "daisies": daisy,
}


for index,word in enumerate(y):
    if word in flowers:
        if index > 0 and y[index-1].isdigit():
            count = int(y[index-1])
        else:
            count = 1
        for _ in range(count):
            flower_functions[word]()  
    else:
       com = com + 1
#Every time the program scans a word and find that it doesnt match with any flower name available it will add a 1 to the variable and at the end of the loop if the variable is equal to the number of words in the input that means we cannot draw the request
if com == com2:

    t.color('red')
    style = ('Courier', 15, 'normal')
    t.write('I am sorry but your request doesnt match with the guidelines \n please put in another prompt, what about some flower drawings like tulips or roses?', font=style, align='center')
    t.hideturtle()

t.done()
