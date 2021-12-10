def triangle():
    print("*")
    print("**")
    print("***")
    print("****")

def square():
    print("*****")
    print("*****")
    print("*****")
    print("*****")

userInput = input("Do you want to print a triangle or a square? ")
userInput2 = input("How many times do you want it to be printed? ")

if (userInput == "triangle"):
    for i in range (int(userInput2)):
        triangle()
elif (userInput == "square"):
    for i in range (int(userInput2)):
        square()