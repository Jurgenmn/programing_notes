people = ["Jack", "Jay", "Jurgen", "Jamal"]

people2 = ["Nick", "Jurgen", "Jamal", "John"]

for names1 in people:
    #print(names1)
    for names2 in people2:
        #print(names2)
        if (names1 == names2):
            #print(names1)
        
#Create a function that takes in two arguments.Argument is gonna be people1 or 2 and name.
#This function needs to check if any of names is repeated twice

# def findName(people, name):
#     for i in people:
#         if(i == name):
#             print(i)
            
# findName(people2, "Jamal") 

#Create a function that takes in two arguments.Argumen is gonna be people1 or 2 and the second one is gonna be the other list.
#This function needs to check if any of names is repeated twice inside the lists

# def repeatedName(a, b):
#     for i in a:
#         for y in b:
#             if (i == y):
#                 print(i)

# repeatedName(people, people2)


# Write a function that takes one argument, and return a list of numbers from 0 - argument.
# Example: generate(3)
#[0, 1,2,]   

def generate(a):
    for i in range(a):
        
    
    return i

print(generate(5))