from typing import ItemsView


def print10():
    for i in range(10):
        print(i)

# print10()


def printdynamic(a, b):
    for i in range(a, b):
        print(i)

# printdynamic(5, 10)


def print_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

# print_even(10, 20)


def find_substring(a, b):
    if a in b:
        return True
    return False

# print(find_substring("Hi", "Hi I am Jamal"))


def find_substring2(a, b):
    words = b.split(" ")
    for word in words:
        if a == word:
            return True
    return False

# print(find_substring2("Hi", "Hi I am Jamal"))


def our_split(substring, sentence):
    words = []
    letters = ""
    for letter in sentence:
        if letter != substring:
            letters = letters + letter
        else:
            words.append(letters)
            letters = ""
    if letters != "":
        words.append(letters)
    return words


# print(our_split("I", "Hi I am Jamal I"))

def str_length(a):
    count = 0
    for i in a:
        count += 1

    return count

# print(str_length("Helloo"))


def ends_with(a, b):
    # last = a[-1]
    last = a[len(a)-1]
    if last == b:
        return True
    return False

# print(ends_with("Hello World", "d"))


def words_end_with(words, string):
    result = []
    for i in words:
        if ends_with(i, string):
            result.append(i)
    return result

# print(words_end_with(["Jack", "Nick", "Jamal"], "k"))


def center(str, char, times):
    new = ""
    for i in range(times):
        new = new + char
    left = new + str
    right = left + new

    return right

# print(center("Hello", "-", 20))


def is_alpha(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i == char.lower():
            return True
    return False


# print(is_alpha("H"))


def is_alpha2(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.lower() in alphabet:
        return True
    return False


# print(is_alpha2("@"))


def is_alpha3(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.lower() in alphabet:
        return True
    return False


# print(is_alpha3("@"))


def is_alpha3(char):
    ascii = ord(char)
    if ascii >= 65 and ascii <= 90:
        return True
    if ascii >= 97 and ascii <= 122:
        return True
    return False


# print(is_alpha3("@"))


def is_alpha4(char):
    ascii = ord(char)
    if ascii >= 65 and ascii <= 90 or ascii >= 97 and ascii <= 122:
        return True
    return False


# print(is_alpha4("#"))

def is_upper(char):
    ascii = ord(char)
    if ascii >= 97 and ascii <= 122:
        return False
    return True


# print(is_upper("o"))


def is_upper2(char):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVXWZ"
    if char in alphabet:
        return True
    return False


# print(is_upper2("w"))


def find_index(word, char):
    index = 0
    for i in word:
        if i == char:
            return index
        index += 1
    return None


# print(find_index("home", "e"))


def find_index2(word, char):
    for i in range(len(word)):
        if word[i] == char:
            return i
    return None


# print(find_index2("home", "o"))


def index(lst, word):
    index = 0
    for i in lst:
        if i == word:
            return index
        index = index + 1
    return None


# print(index(["Jack", "John", "Peter"], "Peter"))


def index2(lst, word):
    for i in range(3):
        if lst[i] == word:
            return i
    return None


# print(index2(["Jack", "John", "Peter"], "Peter"))


def count(lst, name):
    count = 0
    for i in lst:
        if i == name:
            count += 1

    return count


# print(count(["Jack", "John", "Peter", "Peter", "Peter"], "Peter"))


def insert(lst, index, name):
    new_lst = []
    for i in range(len(lst)):
        if i == index:
            new_lst.append(name)
            new_lst.append(lst[i])
        else:
            new_lst.append(lst[i])

    return new_lst


# print(insert(["Jack", "John", "Peter"], 1, "David"))


def reverse(lst):
    new_lst = []
    last_element = lst[len(lst) - 1]
    for i in lst:
        if i == last_element:
            new_lst.append
            last_element -= 1


def extend(lst1, lst2):
    for i in lst2:
        lst1.append(i)

    return lst1


# print(extend(["Audi", "Opel", "Peugeot"], ["Seat", "Fiat", "Citroen"]))


def items(obj):
    lst = []
    for i in obj:
        value = obj[i]
        lst.append([i, value])

    return lst


# print(items({"brand": "Ford", "model": "Mustang", "year": 1964}))


def update(obj, obj2):
    for key in obj2:
        value = obj2[key]
        obj[key] = value

    return obj


# print(update({"brand": "Ford", "model": "Mustang",
    # "year": 1964}, {"color": "White"}))


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


def pop_last(obj):
    last = ""
    for key in obj:
        last = key
    obj.pop(last)
    return obj


# print(pop_last(car))


def pop(obj_car, key):
    obj_car_new = {}
    for i in obj_car:
        if i != key:
            value = obj_car[i]
            obj_car_new[i] = value

    return obj_car_new


#print(pop(car, "year"))
# print(car)


def pop2(obj_car, key):
    del obj_car[key]
    return obj_car


#print(pop2(car, "year"))
# print(car)


def get(obj, key):
    if key in obj:
        value = obj[key]
        return value
    else:
        return None


#print(get(car, "name"))

def get2(obj, key):
    for i in obj:
        if i == key:
            value = obj[i]
            return value
    return None


print(get2(car, "year"))
