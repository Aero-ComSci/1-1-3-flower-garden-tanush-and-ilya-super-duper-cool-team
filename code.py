flowers = {"rose", "lily", "sunflower", "daisy", "tulip"}
x = input("Pick some flowers (separate by spaces): ").lower()  
y = x.split()  

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
    "sunflower": sunflower,
    "daisy": daisy,
    "lily": lily,
    "rose": rose
}

# Process each word in the input
for word in y:
    if word in flowers:
        print("Yea")
        flower_functions[word]()  # Call the function associated with the flower name
    else:
        print("No")
        
