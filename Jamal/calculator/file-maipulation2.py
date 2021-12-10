# f = open("./file-manipulation-text", "r")
# ​
# lines = f.readlines()
# def find_name(first_letters):
#     for line in lines:
#         if first_letters in line:
#             print(line)

f = open("./test", "r")
# print(f.name)
​
lines = f.readlines()
#print(lines)
def find_name(first_letters):
    for line in lines:
        if first_letters in line:
            print(line)
            
            
def changeName():
    for i in lines:
        if(i == "jamal\n"):
            print("We got Jamal")
      
      
#changeName()            
​
#find_name("jas")
# find_name("jam")
# find_name("jay")
​
def findPerson(a):
    for i in lines:
        if (i == a):
            print("we got" + a)
​
#findPerson("john\n")
            
Create a function thatis gonna take an argument,
that is gonnna loop over the lines and if a line
matches the argument then add it to a list
​
2. Create a function thatis gonna take an argument,
that is gonnna loop over the lines and if a line
matches the argument count how many times matches on the list            