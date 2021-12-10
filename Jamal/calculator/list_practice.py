people = ["Jack", "Jay", "Jurgen", "Jamal"]

people2 = ["Nick", "Jurgen", "Jurgen", "Jamal", "John"]


def findName(people, name):
    countName = 0
    for i in people:
        if(i == name):
            countName = countName + 1
            
            
    return countName
            
#print(findName(people2, "Jurgen"))


def repeatedName(a, b):
    for i in a:
        if findName(a, i) > 1:
            return findName(a, i)
        if findName(b, i) > 1:
            return findName(b, i)
            
                
#print(repeatedName(people, people2))

def findRepeatedName(a, b):
    repeatedPeople = []
    for i in a:
        if findName(a, i) > 1:
            repeatedPeople.append(i)
    for y in b:
        if findName(b, y) > 1:
            repeatedPeople.append(y)
            
    return repeatedPeople
        
newList = findRepeatedName(people, people2)
#print(newList)       

def generate(a):
    newList2 = []
    for i in range(a):
        newList2.append(i)
    
    return newList2

#print(generate(5))

# Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def oddEven(a):
    oddNumbers = 0
    evenNumbers = 0
    for i in a:
        if(i % 2 == 0):
            evenNumbers = evenNumbers + 1
        else:
            oddNumbers = oddNumbers + 1
            
    return  [evenNumbers, oddNumbers]

#print(oddEven(numbers))


            
names = ["Jack", "Jay", "Jurgen", "Jamal", "Jurgen", "David", "Thomas", "Martin"]
 
person = {
     "name": "Jack",
     "age": 20
     }
 
person["name"]
 #person.name
 
person["name"] = "Nick"
 #person.name = "Nick"
 
def countNames(a):
    newObj = {}
    for i in a:
        if newObj.get(i):
            newObj[i] = newObj[i] + 1
        else:
            newObj[i] = 1
            
    return newObj


#print(countNames(names))  
         
         
# Create a function that takres in one argument wich is goint to be a list of names and form loopin over the list
# it going to create an object with 2 properties. One properties is coolnames, second properties is badnames.
# How many coolnames and badnames are in the list, and return an object with number of coolnames and badnames.
# Names that starts with letter J are cool names an d others are badnames.

# Ex. findCoolNames(names)
#     {"coolnames": 4, "badnames": 0}
    
# def findCoolNames(a):

# def my_func(names):
#     obj = {"coolNames": 0, "badNames": 0}
#     for name in names:
#         if name.startswith("J"):
#             obj["coolNames"] = obj["coolNames"] + 1
#         else:
#             obj["badNames"] = obj["badNames"] + 1
            
#     return obj

# print(my_func(names))

# number = 10
# number.bit_length()

def func(a):
    newNameList = []
    for i in a:
        if i != "Jay":
            newNameList.append(i)
            
    return newNameList

#print(func(names))   

def func2(array, name):
    newNameList = []
    for i in array:
        if i != name:
            newNameList.append(i)
        
    return newNameList

#print(func2(names, "Jay"))

def func3(array, index):
    newNameList = []
    for i in range(len(array)):
        if i != index:
            newNameList.append(array[i])  #is pushing a name not a number
            
    return newNameList

#print(func3(names, 2))  

name = ["Jack", "Jamal", "Jamal"]

#print(name[1])

def func4(array, number):
    newNameList = []
    for i in range(len(array)):
        if i < number:
            newNameList.append(array[i])
            
    return newNameList

#print(func4(names, 5))  

def func4(array, number):
    newNameList = []
    for i in range(number):
        newNameList.append(array[i])
            
    return newNameList

#HOME WORK

def func5(array, name):
    newNameList = []
    for i in range(len(array)):
        if(i % 2 == 0):  # we need to loop over an integer not over a name( see the line above)
            newNameList.append(name)
        else:
            newNameList.append(array[i])
    
    return newNameList
        
                
#print(func5(names, "Nick"))
#["Jack", "Nick", "Jay", "Nick", "Jamal", ]   

def func6(array, number, name):
    newNameList = []
    for i in range(len(array)):
        if i == number:
            newNameList.append(name)
        else:
            newNameList.append(array[i])
    
    return newNameList        
    
#print(names)    
#print(func6(names, 2, "Nick"))
#["Jack", "Jay", "Nick".....]  

def func7(array, number, name):
    newNameList = []
    for i in range(len(array)):
        if i == number:
            newNameList.append(name)
            newNameList.append(array[i])
        else:
            newNameList.append(array[i])
    
    return newNameList        
    
#print(names)    
#print(func7(names, 2, "Nick"))
#["Jack", "Jay", "Nick".....]   


def func8(array, number):
    myName = array[number] #variable that holds the string jurgen
    counter = 0
    for i in array:
        if i == myName:
            counter = counter + 1
    
    return counter

#print(func8(names, 2))

def func9(array, name1, name2):
    counterFirstName = 0
    counterSecondName = 0
    for i in array:
        if(i == name1):
            counterFirstName = counterFirstName + 1
        elif(i == name2):
                counterSecondName = counterSecondName + 1
                
    return [counterFirstName, counterSecondName] # to retrun 2 or more elements create a list         
    
#print(func9(names, "Jurgen", "Jamal"))

def func10(array, number1, number2):
    firstName = array[number1]
    secondName = array[number2]
    counterOne = 0
    counterTwo = 0
    for i in array:
        if i == firstName:
            counterOne = counterOne + 1
        elif i == secondName:
            counterTwo = counterTwo + 1
              
    return [counterOne, counterTwo]

#print(func10(names, 2, 3)) 

def func11(array):
    counter = 0
    for i in array:
        counter = counter + 1
        
    return counter

#print(func11(names))

#print(len(names)) #second way of doing it


resault = func11(names)
#print(resault)

resault2 = len(names)
#print(resault2)

def func12(name, age, haircolor):
    person = {"name": name, "age": age, "haircolor": haircolor}
    
    return person

person1 = func12("Jurgen", 12, "brown")

#print(person1)

def func13(personObj, height):
    personObj["height"] = height #name of the property and the value
    
    return personObj
    
    
#print(func13(person1, 150))

#Home Work
names = ["Jack", "Jay", "Jurgen", "Jamal", "Jurgen", "David", "Thomas", "Martin"]

def func14(array, name, number):
    newList = []
    for i in range(len(array)):
        if i == number:
            newList.append(array[i])
            newList.append(name)
        else:
            newList.append(array[i])   
            
    return newList        
    
       
#print(func14(names, "Nick", 4))
#["Jack", "Jay", "Jurgen", "Jamal", "Jurgen", "Nick" "David", "Thomas", "Martin"]   

def func15(array, name): #Add the name to the beginig and to the end of the array
    newList = []
    for i in array:
        newList.insert(0, name)
        newList.append(i)
        
    newList.append(name)
        
    return newList

#print(func15(names, "Maximilian"))

def func16(array, name):
    newList = [name]
    for i in array:
        newList.append(i)
        
    newList.append(name)
        
    return newList

#print(func16(names, "Maximilian"))

# Write a function that takes an array of names (strings) and a string as the second argument.
# This function will check if any of the names in the array starts with the string in the second argument.
# func20([“jack”, “jay”, “nick”], “ja”)
# [“jack”, “jay”]

def func17(array, letters):
    count = 0
    for i in array:
        if i.startswith(letters):
            count = count + 1
            
    return count


resault = func17(["jack", "jay", 'nick'], "n")
#print(resault)

def func18(array, name):
    newList = [name, name]
    for i in array:
        newList.append(i)
        
    return newList
    
#print(func18(["jack", "jay", 'nick'], "Jamal"))
#["Jamal", "Jamal", "Jack"....]

def func19(array, name):
    newList = []
    for i in array:
        newList.append(i)
        
    # newList.append(name)  
    # newList.append(name)
    #names = [name, name]
    newList.extend([name, name])
    
    
    return newList


#print(func19(["jack", "jay", 'nick'], "Jamal"))

def func20(array, name):
    newList = []
    middle = len(array) // 2
    for i in range(len(array)):
        if i == middle:
            newList.append(name)
            newList.append(name)
            
            
        newList.append(array[i])
            
            
    return newList

#print(func20(["jack", "jay", 'nick'], "Jamal"))

#Home Work

nameList = ["jack", "jay", 'nick']

def func21(array, number, name):
    newList = []
    for i in range(len(array)): 
        newList.append(array[i])
        if i == number:
            newList.append(name)
            newList.append(name)

    
    return newList

#print(func21(nameList, 1, "Jamal"))     #After index 1 add name twice

#["jack","Jamal", "Jamal" "jay", 'nick'] 

def func22(array, number): #Filter the element at that index
    newList = []
    for i in range(len(array)):
        if i != number:
            newList.append(array[i])
    
    return newList
    
    
#print(func22(["jack", "jay", 'nick'], 1))    #try to use pass to


def func23(array, number):
    newList = []
    for i in range(len(array)):
        if i == number:
            pass
        else:
            newList.append(array[i])
            
    return newList

#print(func23(["jack", "jay", 'nick'], 1))


obj1 = {"name": "Jack", "age": 26}
obj2 = {"name": "Nick", "age": 27}
obj3 = {"name": "Jamal", "age": 28}
obj4 = {"name": "Jurgen", "age": 29}

people = [obj1, obj2, obj3, obj4]

def func24(person1, person2):
    if person1["age"] == person2["age"]:
        return True
    
  
    return False   

#print(func24(obj1, obj2))

def func25(array):
    newList = []
    for i in array:
        if i["age"] > 27:
            newList.append(i)
            
    return newList    


#print(func25(people))

def func26(array, number):
    newList = []
    for i in array:
        if i["age"] > number:
            newList.append(i)
            
    return newList
        
#print(func26(people, 28))

def func27(array, person, number):
    newList = []
    for i in range(len(array)):
        if i == number:
            newList.append(person)
            
        newList.append(array[i])
        
    return newList    
          
    
#print(func27(people, {"name": "Nick", "age": 27}, 1))

def func28(array, number, name):
    newList = []
    for i in array:
        if i["age"] > number and i["name"].startswith(name):    #Kjo do te jape emrin
            newList.append(i)                                                 # This is gonna give the string
            
    return newList        
    
       
#print(func28(people, 27, "Ja"))  #Do the ignor casing


def func29(array, number, letter):
    newList = []
    for i in array:
        lowerCaseName = i["name"].lower()
        
        if i["age"] > number and lowerCaseName.startswith(letter.lower()):
            newList.append(i)
            
    return newList

#print(func29(people, 27, "jA"))        

#Home Work

names = ["Jack", "Nick"]
newNames = names
ages = [27, 28]  

def func30(alises, ages): #From 2 names and ages constract 2      #alises = names
    obj1 = {"name": alises[0], "age": ages[0]}
    obj2 = {"name": alises[1], "age": ages[1]}
    
    return [obj1, obj2]
   
#print(func30(names, ages))   
#[{"name": "Jack", "age": 27}, {"name": "Nick", "age": 28}]

def func30(alises, ages):
    newList = []                                  #From 2 names and ages constract 2      #alises = names ###You dont use global variables inside a function instead you pass it as argument in function arguments
    for i in range(len(alises)):
        obj = {"name": alises[i], "age": ages[i]}
        newList.append(obj)
        
    return newList

   
#print(func30(names, ages))

# Write a function that takes 2 arguments and returns a list of all odd numbers in both lists :

def find_odd(list_a, list_b):
    oddNumbers = []
    for i in list_a:
        if (i % 2 != 0):
            oddNumbers.append(i)   # It's working but I dont think is good putting 2 for loops one after another
    for y in list_b:
        if (y % 2 != 0):
            oddNumbers.append(y)
            
    return oddNumbers        
                    
    
#print(find_odd([1, 2, 3, 4], [9, 8, 7, 6, 5]))
# [1,3,9,7,5]

def find_odd(list_a, list_b):
    oddNumbers = []
    for i in list_a:
        if (i % 2 != 0):
            oddNumbers.append(i)   # It's working but I dont think is good putting 2 for loops one after another
    for y in list_b:
        if (y % 2 != 0):
            oddNumbers.append(y)
            
    return oddNumbers        
                    
    
#print(find_odd([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))
# [1,3,9,7,5]

def find_odd2(list_a, list_b):
    oddNumbers = []
    for i in range(len(list_a)):
        if list_a[i] % 2 != 0:
            oddNumbers.append(list_a[i])
        if list_b[i] % 2 != 0:    
            oddNumbers.append(list_b[i])
            
    return oddNumbers        
                    
    
#print(find_odd2([1, 2, 3, 4], [9, 8, 7, 6, 5]))

# For example: find_odd([1,2,3], [1,3,4])
# Will return [1,3,1,3]
# Can you make it so that it only return unique numbers like: [1,3]

def func_UniqOdd(list_a, list_b):
    uniqueList = []
    resault = find_odd2(list_a, list_b)
    print(resault)
    for i in resault:
        if i not in uniqueList:
            uniqueList.append(i)
            

    return uniqueList

#print(func_UniqOdd([1,2,3], [1,3,4]))

def func31(numbers):
    firstNum = numbers[0]
    counter = 0
    secondNum = 0
    for i in numbers:
        if firstNum == i:   #i is the current element because we are not doing range
            counter = counter + 1
        elif counter > 1:
            secondNum = i
                
        
    return secondNum
    
      
#print(func31([2,2,2,2,5,2,2,2,2,]))

def func31(numbers):
    firstNum = numbers[0]
    for i in numbers:
        if firstNum == i:
            pass
        else:
            return i
    
      
#print(func31([2,2,2,2,5,2,2,2,2,]))


def func32(names, name):
    for i in names:
        if i == name:
            return True
        
    return False
    
#print(func32(["Jamal", "Jurgen", "Jack"], "Jack"))

def func33(names1, names2):
    newList = []
    for i in names1:
        if func32(names2, i ):
            newList.append(i)
            
    return newList    
    
    
#print(func33( ["Jack", "Nick", "Jamal"]))    
    
#How to create alises

#Function Composition (using functions inside other functions)

def func34(names, personObj):
    name = personObj["name"]
    resault = func32(names, name)
    
    
    return resault
    
  
#print(func34(["Jamal", "Jurgen", "Jack"], {"name": "Jurgen", "age": 22}))

def func35(obj1, obj2):
    nameObj1 = obj1["name"]
    nameObj2 = obj2["name"]
    ageObj1 = obj1["age"]
    ageObj2 = obj2["age"]
    if nameObj1 == nameObj2 and ageObj1 == ageObj2:
        return True
    

    return False
    
#print(func36({"name": "Jurgen", "age": 22}, {"name": "Jurgen", "age": 22})) 

def func36(obj1, obj2):
    return obj1["name"] == obj2['name'] and obj1["age"] == obj2["age"]  #Operators True and False = False   True or False = True
    
#print(func36({"name": "Jurgen", "age": 22}, {"name": "Jurgen", "age": 22}))

def func37(array, obj):
    for i in array:
        if func36(i, obj):
            return True
            
    return False    
     
    
#print(func37([{"name": "Jurgen", "age": 22}, {"name": "David", "age": 23}, {"name": "Jack", "age": 20}], {"name": "David", "age": 23}))


def func38(array1, array2): #1 st way
    newList = []
    for i in range(len(array1)):
        if func37(array1, array2[i]):
            newList.append(array2[i])
    
    
    return newList
    
people1 = [{"name": "Jurgen", "age": 22}, {"name": "David", "age": 23}, {"name": "Jack", "age": 20}]
people2 = [{"name": "John", "age": 26}, {"name": "David", "age": 23}, {"name": "Jack", "age": 20}]

#print(func38(people1, people2))

def func39(array1, array2): #2 nd way
    newList = []
    for i in array2:
        if func37(array1, i):
            newList.append(i)
            
    return newList

#print(func39(people1, people2))  



def func40(names, name):
    for i in range(len(names)):
        if names[i].upper() == name.upper():
            return i
    return -1
   
#print(func40(["Jamal", "Jurgen", "David"], "dAvid"))        
        

def func41(names):
    people = {"Jamal": 0, "Jurgen": 0, "David": 0}
    for i in names:
        if i == "Jamal":
            people["Jamal"] = people["Jamal"] + 1
        if i == "Jurgen":
           people["Jurgen"] = people["Jurgen"] + 1
        if i == "David":
            people["David"] = people["David"] + 1
        
    return people        
           
# print(func41(["Jamal", "Jurgen", "Jurgen", "David", "Nick"]))


def func42(names):
    people = {"Jamal": 0, "Jurgen": 0, "David": 0}
    for i in names:
        if i == "Jamal" or i == "Jurgen" or i == "David":
            people[i] = people[i] + 1
 
        
    return people        
           
#print(func42(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"]))


def func43(names):
    people = {}  
     
    for i in names:
        if people.get(i) != None and people.get(i) >= 0:
            people[i] = people[i] + 1
        
        else:
            people[i] = 1    
        
    return people

#print(func43(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"]))


#Home Work

def func44(names, name):
    obj = {name: 0}
    for i in names:
        if i == name:
            obj[name] = obj[name] + 1
            
    return obj        
    
      
#print(func44(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], "Jurgen"))  #How many times is Jurgen is mentioned in array 
#{"Jurgen": 3}

def func45(names, idx):
    name = names[idx]
    obj= {name: 0}
    for i in range(len(names)):
        if name == names[i]:
            obj[name] = obj[name] + 1
    
    return obj

#print(func45(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], 1))  #How many times is the string at index x is mentioned in array 


def func46(names, idx): #Simplified
    name = names[idx]
    obj= {name: 0}
    for i in names:
        if i == name:
            obj[name] = obj[name] + 1
    
    return obj

#print(func46(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], 1))

#print(func46(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], 1))  #How many times is the string at index x is mentioned in array 

def func47(names, name, name2):
    person1 = func44(names, name)
    person2 = func44(names, name2)
    person1.update(person2)
    #print(person1, person2)
    return person1
                
#print(func47(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], "Jurgen", "Jamal"))
#{"Jurgen": 3, "Jamal": 1}  

def func48(names, name, name2):
    obj = {name: 0, name2: 0}
    for i in names:
        if i == name:
            obj[name] = obj[name] + 1
        if i == name2:
            obj[name2] = obj[name2] + 1 
            
    return obj

#print(func48(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], "Jurgen", "Jamal"))


def func49(names, idx1, idx2):
    person1 = names[idx1]
    person2 = names[idx2]
    obj = {person1: 0, person2: 0}
    for i in names:
        if i == person1:
            obj[i] = obj[i] + 1
        if i == person2:
            obj[i] = obj[i] + 1
            
    return obj            
    
#print(func49(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], 1, 0))  

def func50(names, idx1, idx2):
    person1 = names[idx1]
    person2 = names[idx2]
    people = func48(names, person1, person2)
    
    return people
    
      
#print(func50(["Jamal", "Jurgen", "Jurgen", "Jurgen", "David", "Nick"], 1, 0))


def generate_numbers(number):
    newList = []
    for i in range(number):
        newList.append(i)
     
    return newList
#print(generate_numbers(3))
#[0, 1, 2]


#Home Work

def find_dublicate(names1, names2): #Find the dublicate names in both arrays and put those names in a new array
    new_list = []
    for i in names2:
        for y in names1:
            #print("i is:", i, "y is:", y)
            if i == y:
                for j in new_list:
                    if i == j:
                        
                        new_list.append(i)
        
    return new_list
    
#print(find_dublicate(["Jamal", "Jurgen", "Jack"], ["Jurgen", "Jay", "Jack", "Jurgen"]))
# "Jack"

def find_dublicate2(names1, names2): #Find first simlar name
    for i in names1:
        for y in names2:
            if i == y:
                return i

    return False #none of the names are in lists
        
        
#print(find_dublicate2(["Jamal", "Jurgen1", "Jack1"], ["Jurgen", "Jay", "Jack"]))

#copy from Slack

def is_exsist(array, name):
    for n in array:
        if n == name:
            return True
    return False
def find_dub(array1, array2):
    new_array = []
    for name1 in array1:
        for name2 in array2:
            # print("name1: ", name1, "name2: ", name2)
            if name1 == name2:
                if is_exsist(new_array, name1) == False:
                    new_array.append(name1)
    return new_array
#print(find_dub(["jack", "jay"], ["jack", "jay", "jay"]))


def addition(a, b):
    return a + b

#print(addition(10, 10))

def find_largest_number(numbers):
    biggest_number = numbers[0]
    for number in numbers:
        if number > biggest_number:
            biggest_number = number
            
    return biggest_number        
    
    
#find_largest_number([5,4,10,7]) 

def find_smallest_number(numbers):
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
            
    return smallest_number        
    
    
#print(find_smallest_number([5,4,10,20,7]))

def find_youngest_person(people):
    youngest_age = people[0]
    for person in people:
        if person["age"] < youngest_age["age"]:
            youngest_age = person
            
    return youngest_age      
    
    
#print(find_youngest_person([{"name": "Jurgen", "age": 34}, {"name": "Jamal", "age": 23}]))  


def find_oldest_person(people):
    oldest_age = people[0]
    for person in people:
        if person["age"] > oldest_age["age"]:
            oldest_age = person
            
    return oldest_age      
    
    
#print(find_oldest_person([{"name": "Jurgen", "age": 34}, {"name": "Jamal", "age": 23}]))


def filter_people(people, age, letter):
    new_list = []
    for person in people:
        if person["age"] > age and person["name"].startswith(letter):
            new_list.append(person)
    
    
    return new_list
    
    
#print(filter_people([{"name": "Jurgen", "age": 34}, {"name": "Jamal", "age": 23}], 25, "J"))

def filter_people2(people, age, letter):
    new_list = []
    for person in people:
        if person["age"] > age or person["name"].startswith(letter):
            new_list.append(person)
    
    
    return new_list
    
    
#print(filter_people2([{"name": "Jurgen", "age": 34}, {"name": "Jamal", "age": 23}], 25, "J"))


def find_all_odd(numbers):
    new_list = []
    for number in numbers:
        if number % 2 != 0:
            new_list.append(number)
        
    return new_list    

    
#print(find_all_odd([1, 4, 2, 5]))

def count_numbers(numbers, target):
    newObj = {}
    for i in target:
        for y in numbers:
            if i == y:
                if newObj.get(i) == None:
                    newObj[i] = 1
                else:    
                    newObj[i] = newObj[i] + 1         
                
    return newObj
    
#print(count_numbers([1,1,2,2,4,6,10], [1, 10]))   

def count_numbers2(numbers, target):
    newObj = {}
    for i in target:
        count = numbers.count(i)
        newObj[i] = count
    return newObj
    
#print(count_numbers2([1,1,2,2,4,6,10], [1, 10])) 

# numbers = [1,1,2,2,4,6,10]
# numbers.count() #works only on arrays thats why is called method


def filter_people3(people, age):
    newList = []
    for person in people:
        print(person)
        if person["age"] > age:
            newList.append(person)
    return newList
    
    
#print(filter_people3([{"name": "Jack", "age": 21}, {"name": "David", "age": 22}], 21))


def filter_people4(people, age):
    younger = []
    older = []
    for person in people:
        if person["age"] < age:
            younger.append(person)
        if person["age"] > age:
            older.append(person)
    return {"younger": younger, "older": older}
            
#print(filter_people4([{"name": "Jack", "age": 20}, {"name": "David", "age": 22}], 21))


def filter_numbers(numbers, condition, number):
    bigger = []
    smaller = []
    for i in numbers:
        if i > number:
            bigger.append(i)
        if i < number:
            smaller.append(i)
            
    if condition == ">":
        return bigger
    
    return smaller
#print(filter_numbers([1, 2, 3, 4, 5, 6], "<", 3))

def filter_numbers(numbers, condition, number):
    result = []
    for i in numbers:
        if condition == ">":
            if i > number:
                result.append(i)
        if condition == "<":
            if i > number:
                result.append(i) 
                
    return result                   
                            
#print(filter_numbers([1, 2, 3, 4, 5, 6], ">", 3))  

def find_name(names, name):
    for i in names:
        if i == name:
            return True
    return False

#print(find_name(["Jay", "Jay", "David"], "David"))  # not part of the code


def filter_dublicates(names):
    new_list = []
    for i in names:
        if i not in new_list:  #if not find_name(new_list, i):
            new_list.append(i)
            
    return new_list        
              
#print(filter_dublicates(["Jay", "Jay", "David"]))


def rm_dup(array): #2nd way
    result = []
    found = False
    for name in array:
        for name2 in result:
            if name == name2:
                found = True
        if not found:
            result.append(name)
        found = False
    return result        
#print(rm_dup(["jay", "jay", "david", "nick"]))

def find_old_person(people):
    oldest = people[0]
    for person in people:
        if person["age"] > oldest["age"]:
            oldest = person
            
    return oldest        
            
   
#print(find_old_person([{"name": "Jay", "age": 20}, {"name": "John", "age": 22}, {"name": "David", "age": 19}])) 


def reverse(name):
    new_name = ""
    for i in range(len(name)):
        new_name = new_name + name[len(name) - i - 1]
        
    return new_name
 
#print(reverse("Jamal"))   


def cut_in_half(name):
    half = len(name) // 2
    first_half = name[: half]
    second_half = name[half : ]

    return second_half + first_half
          
#print(cut_in_half("Hello")) 

def cut_list(names):
    half = len(names) // 2
    half1 = names[: half]
    half2 = names[half: ]
    
    return half2.merge(half1)
    
    
#print(cut_in_half(["Hello", "David", "John"]))

def cut_names(names):
    new_list = []
    for i in names:
        item = cut_in_half(i)
        new_list.append(item)
    
    return new_list
    
#print(cut_names(["Hello", "David", "John"]))

def replace_vowel(string):
    vowels = "iuaeo"
    new_string = ""
    for i in string:
        if i in vowels:
            new_string = new_string + "h"
        else:
            new_string = new_string + i
    
    return new_string

#print(replace_vowel("Hello"))

# HOW TO ADD VALUE TO A KEY IN AN OBJECT

def count_names(lst):
    new_obj = {}
    for i in lst:
        new_obj[i] = 0
    for j in lst:
        new_obj[j]  = new_obj[j] + 1
    
    return new_obj
 
#print(count_names(["Jack", "Jay", "Nick","Jay", "John"]))
# {"Jack": 1, "Jay": 2, "Nick": 1.....}    

#*******************************
def countNames(a):
    newObj = {}
    for i in a:
        if newObj.get(i):
            newObj[i] = newObj[i] + 1
        else:
            newObj[i] = 1
            
    return newObj


#print(countNames(names))

from random import randint

def generate_password():
    password = ""
    for i in range(8):
        random_num =str(randint(0, 9))
        password += random_num
    
    return password
#print(generate_password()) 

#Add letters to the password 
def generate_password():
    letters = "0123456789abcdefd"
    password = ""
    for i in range(8):
        random_num =randint(0, len(letters) - 1)
        
        password += letters[random_num]
    
    return password
#print(generate_password())

#Make this function take a length argument and generate a password of that

def generate_password(number):
    letters_numbers = "0123456789abcdefghijklmnopqrstvuxz"
    password = ""
    while len(password) < number:
        random_num = randint(0, len(letters_numbers) - 1) 
        charachter = letters_numbers[random_num]
        if charachter.isdigit():
            if charachter not in password:
                password += letters_numbers[random_num]  
        else:
               password += letters_numbers[random_num]   
        
    return password

#print(generate_password(8))

def generate_password2(lst, num):
    letters_numbers = "0123456789abcdefghijklmnopqrstvuxz"
    password = ""
    while len(password) < num:
        random_num = randint(0, len(letters_numbers) - 1) 
        charachter = letters_numbers[random_num]
        if charachter not in lst:
            password += letters_numbers[random_num]  
        
    return password
       
#print(generate_password2(["a", "b", "3"], 4))


def password_generator3(length, num):
    password_list = []
    while len(password_list) < num:
    #for i in range(num):
        password = generate_password(length)
        password_list.append(password)
        
    return password_list    
        
#print(password_generator3(2, 20))

store = []

def password_generator4(length, num):
    password_list = []
    while len(password_list) < num:
    #for i in range(num):
        password = generate_password(length)
        if password not in store:
            password_list.append(password)
            store.append(password)
        
    return password_list    
        
# print(password_generator4(4, 10))
# print(password_generator4(4, 10))
# print(password_generator4(4, 10))

# print(store)

def is_harshad(num):
    sum = 0
    string = str(num)
    for i in string:
        integer = int(i)
        sum += integer
          
    if num % sum == 0:
        return True
    else:
        return False        

#print(is_harshad(171))

def write_to_file(file_name, string):
    handler = open(file_name, "w")
    handler.write(string) 
    
#write_to_file("test.txt", "This is a new string\n")

def add_to_file(file_name, string):
    handler = open(file_name, "a") # mode
    handler.write(string)
    
#add_to_file("test.txt", "This is an added sting\n")

def save_new_password(file_name):
    password = generate_password(8)
    add_to_file(file_name, password + "\n")
    
#save_new_password("test.txt")

def save_new_passwords(file_name, num_pass):
    passwords = password_generator3(4, num_pass)
    for password in passwords:
        add_to_file(file_name, password + ", \n " )
      
#save_new_passwords("test.txt", 8)

def save_new_passwords2(file_name, num_pass):
    for i in range(num_pass):
        save_new_password(file_name)
        
#save_new_passwords2("test.txt", 8)

def save_new_passwords3(file_name, num_pass):
    i = 0
    while i < num_pass:
        save_new_password(file_name)
        i += 1
        save_new_passwords3("test.txt", 8)

#HOME WORK
def save_formated_password(file_name):
    i = 0
    while i < 5:   # i < 1 if we want to loop just one time
        password = generate_password(8)
        add_to_file(file_name, "[ - " + password + " - ]" + "\n")
        i += 1
        
#save_formated_password("test.txt")

def save_formated_password2(file_name, num):
    for i in range(num):
        password = generate_password(8)
        add_to_file(file_name, "[-" + password + "-]" + "\n")
        
#save_formated_password2("test.txt")   
"[-12323-]"

def random_pasword(number):
    save_formated_password2("test.txt", number)
    
#random_pasword(3)

def check_for_duplicate(string):
    for i in string:
        if i == "-":
            continue
        if string.count(i) > 1:
            #print(i)
            return True
    return False    

def test_password(lst):
    for password in lst:
        if not len(password) >= 12: #if len(password) < 12:
            print("A", password)
            return False
        if not (password[0] == "[" and password[1] == "-" and password[len(password) - 2] == "-" and password[len(password)- 1] == "]"):
            print("B", password)
            return False
        if check_for_duplicate(password):
            print("C", password)
            return False   
            
    return True
                
    
#print(test_password(["[-12345678-]", "[-87654321-]"])) 

#READING LINES ON A FILE

def read_file(file_name):
    handler = open(file_name, "r")
    lines = handler.readlines()
    
    return lines

#print(read_file("test.txt"))

#random_pasword(10)

def validate_file(file_name):
    lines = read_file(file_name)
    #print(lines)
    newList = []
    for i in lines:
        #newList.append(i[:-1])
        newList.append(i[:len(i) - 1])
    print(newList)
    validate_lines = test_password(newList)
    
    return validate_lines

print(validate_file("test.txt"))



