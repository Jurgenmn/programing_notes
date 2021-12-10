

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

def triangle_square(a, b, c):
    for i in range(a):
        triangle()
    for i in range(b):   
        square()
    for i in range(c):   
        circle()

# triangle_square(5, 2, 3)


def fullName():
    return "Jamal Al"

name = fullName()

# print(name)

def fetchUsers():
    # print("We are fetching data from google")
    return ["Jamal", "Jurgen", "Jack"]

people = fetchUsers()    
print(people)

# for person in people:
    # print(person)

for i in range (len(people)):
    print (people[i]) 

# create a function and this function is goona ask the user in the console "What is your first name?"
# the user is gonna type the name
# the function will return the first name
# create another function that asks the user for his last name and the user is gonna type his last name in console
# the function will return the last name
# Call the first and second function and take te return value and concatenate together the string and print it to the console.

def firstName():
    ask1 = input("What is your first name? ")
    return ask

def lastName():
    ask2 = input("What is your last name? ")
    return ask2

name = firstName()
surname = lastName()

print("My full name is " + name + surname)
