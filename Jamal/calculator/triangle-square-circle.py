def triangle():
    print("   /\    ")
    print("  /  \   ")
    print(" /    \  ")
    print("/______\ ")

def square():
    print(" _______ ")
    print("|       |")
    print("|       |")
    print("|_______|")

def circle():
    print("   ____   ")
    print(" /      \ ")
    print("|        |")
    print(" \ ____ / ")  

userInput1 = input("What geometric shape do yo want to print? ")
userInput2 = input ("How many time do you want to print the geometric shape/shapes? ")

if (userInput1 == "triangle"):
    for i in range (int(userInput2)):
        triangle()
if (userInput1 == "square"):
    for i in range (int(userInput2)):
        square()
if (userInput1 == "circle"):
    for i in range (int(userInput2)):
        circle()
if (userInput1 == "triangle, square"):
    for i in range (int(userInput2)):
        triangle()
        square()
if (userInput1 == "triangle, square, circle"):
    for i in range (int(userInput2)):
        triangle()
    for i in range (int(userInput2)):
        square()
    for i in range (int(userInput2)):
        circle()
