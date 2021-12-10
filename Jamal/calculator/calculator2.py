
while(True):
    val1 = input("Enter the first number: ")
    val2 = input("Enter the second number: ")
    action = input("What would you like to do? + - * / +- : ")

    print(val1)
    print(val2)
    print(action)

    if(action == ""):
        break
    elif(action == "+"):
        print(int(val1) + int(val2))
    elif(action == "-"):
        print(int(val1) - int(val2))
    elif(action == "*"):
        print(int(val1) * int(val2))
    elif(action == "/"):
        print(int(val1) / int(val2))
    elif(action == "+-"):
        print(int(val1) + int(val2))
        print(int(val1) - int(val2))
        