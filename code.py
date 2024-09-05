flowers = {"rose", "lily", "sunflower", "daisy", "tulip","roses", "lilies", "sunflowers", "daisies", "tulips"}
x = input("Pick some flowers (separate by spaces): ").lower()  
y = x.split() 
com2 = len(y) 
com = 0
def tulip():
    print("drawing a tulip")
def sunflower():
    print("drawing a Sunflower")
def daisy():
    print("drawing a daisy")
def lily():
    print("drawing a lily")
def rose():
    print("drawing a rose")
    
flower_functions = {
    "tulip": tulip,
    "tulips": tulip,
    "sunflower": sunflower,
    "sunflowers": sunflower,
    "daisy": daisy,
    "daisies": daisy,
    "lily": lily,
    "lilies": lily,
    "rose": rose,
    "roses": rose,
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
    print("I am sorry but your request doesnt match with the guidelines please try another flower")
