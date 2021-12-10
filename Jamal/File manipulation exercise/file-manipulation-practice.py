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


          
# 1st Exercise
def pushName(a):
    newList = []
    for i in lines:
        if (i == a):
            newList.append(a)
            print(newList)

pushName("Jurgen\n")

# 2nd Exercise

def addNames(a):
    sum = 0
    for i in lines:
        if(i == a):
            sum = sum + 1
            print(sum)

addNames("Jamal\n")