while (True):
    val1 = input("enter first value: ")
    val2 = input("enter second value: ")
    action = input("What would you like to do? - + * /: ")
​
     print(val1)
     print(val2)
     print(action)
    if(action == ""):
        break
    elif(action == "*"):
        print(int(val1) * int(val2))
        print(mul(val1, val2))
    elif(action == "-"):
        print(int(val1) - int(val2))
    elif(action == "+"):
        print(int(val1) + int(val2))
    elif(action == "/"):
        print(int(val1) / int(val2))