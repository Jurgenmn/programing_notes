def firstName():
    ask1 = input("What is your first name? ")
    print(ask1) #Optional
    return ask1

def lastName():
    ask2 = input("What is your last name? ")
    print(ask2) #Optional
    return ask2

name = firstName()
surname = lastName()

print("Your full name is " + name + " " + surname)

