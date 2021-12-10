file = open("./name-list", "r")

#print(file.name)

lines = file.readlines()
print(lines)

def find_name(first_letters):
    for i in lines:
        if first_letters in lines:
            print(i)

#find_name("Jur")

def findPerson(a):
    for i in lines:
        if (i == a):
            print(a)
            
#findPerson("Jurgen\n")  

def findName2():
    for i in lines:
        if(i == "David\n"):
            print(i)

#findName2()

# HomeWork
# 1. Create a function thatis gonna take an argument,
# that is gonnna loop over the lines and if a line
# matches the argument then add it to a list

# 2. Create a function thatis gonna take an argument,
# that is gonnna loop over the lines and if a line
# matches the argument count how many times matches on the list
          
# 1st Exercise
def pushName(a):
    newList = []
    for i in lines:
        if (i == a):
            newList.append(a)
           
    return newList

newList = pushName("Jurgen\n")
#print(newList)

# 2nd Exercise

def addNames(a):
    sum = 0
    for i in lines:
        if(i == a):
            sum = sum + 1
    
    return sum

#print(addNames("Jamal\n"))

#addNames("Jamal\n")

# Ok this is easy as well, do you see how we check for the 
# name now “if(i == "David\n"):” we have to include the “\n” or otherwise 
# it doesn’t work. Can you create a function that will go over all the names 
# and remove the “\n” and appended the new names to a new list

def removeSymbolAfterName(a, b, c):
    newList = []
    for i in lines:
        if(i == a or i == b or i == c):
            newList.append(i[:-1])
        
    return newList

newList = removeSymbolAfterName("Jurgen\n", "Jamal\n", "Francesco\n")
print(newList)