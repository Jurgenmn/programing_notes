#1st way
import math
def number_split(a):
    half = a / 2
    #print(half)
    if a % 2 == 0:
        return [math.floor(half), math.floor(half)]
    else:
        return [math.floor(half), math.ceil(half)]
    
result = number_split(10)
#print(result)

#2nd way
import math
def number_split2(a):
    half = a // 2
    #print(half)
    if a % 2 == 0:
        return [half, half]
    else:
        return [half, half + 1]
    
result = number_split2(10)
#print(result)


def how_many_vowels(n):
    vowels = "aeiou"
    count_vowels = 0
    for letter in vowels:
        for letter2 in n:
            if letter == letter2.lower():
                count_vowels = count_vowels + 1
                
    return count_vowels
    
print(how_many_vowels("Celebration"))


# def calculator(a, b):
#     userInput = input("")