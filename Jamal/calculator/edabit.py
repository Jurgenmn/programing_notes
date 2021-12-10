from typing import NewType
import math


def remainder(a, b):
    return a % b

# print(remainder(8, 3))


def string_int(a):
    return int(a)

# print(string_int("10"))


def how_many_seconds(a):
    minutesInHour = 60
    secondsInMinutes = 60
    return (a * minutesInHour * secondsInMinutes)


hours = 3
result = how_many_seconds(hours)
# print("There are " + str(result) + " seconds in " + str(hours) + " hours" )


# Home Work

def number_split(a):  # 1st way
    half = a / 2
    # print(half)
    if a % 2 == 0:
        return [math.floor(half), math.floor(half)]
    else:
        return [math.floor(half), math.ceil(half)]


result = number_split(-9)
# print(result)


def number_split2(a):  # 2nd way
    half = a // 2
    # print(half)
    if a % 2 == 0:
        return [half, half]
    else:
        return [half, half + 1]


result = number_split(-9)
# print(result)


def how_many_vowels(n):
    vowels = "aeiou"
    count_vowels = 0
    for letter in vowels:
        for letter2 in n:
            if letter == letter2.lower():
                count_vowels = count_vowels + 1

    return count_vowels

# print(how_many_vowels("Aelebration"))


def how_many_vowels2(n):
    vowels = "aeiou"
    count_vowels = 0
    for letter in n:
        if letter.lower() in vowels:
            count_vowels = count_vowels + 1

    return count_vowels

# print(how_many_vowels2("Aelebration"))


def calculator(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    if operator == "-":
        return number1 - number2
    if operator == "/":
        return number1 / number2
    if operator == "*":
        return number1 * number2


# print(calculator(2, "*", 2))


def find_smallest_number(numbers):
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


def remove_number_from_list(numbers, number):
    new_numbers_list = []
    for i in numbers:
        if i != number:
            new_numbers_list.append(i)

    return new_numbers_list


def sort(numbers):
    new_list = []
    for i in range(len(numbers)):
        smallest_number = find_smallest_number(numbers)
        new_list.append(smallest_number)
        numbers = remove_number_from_list(numbers, smallest_number)

    return new_list


# print(sort([1, 10, 20, 4, 6]))


def find_youngest(people):
    youngest = people[0]
    for person in people:
        if person["age"] < youngest["age"]:
            youngest = person["age"]

    return youngest


def remove_person_from_list(people, person):
    new_people_list = []
    for i in people:
        if i["name"] != person["name"] and i["age"] != person["age"]:
            new_people_list.append(i)

    return new_people_list


def sort_people(people):
    new_list = []
    for i in range(len(people)):
        youngest = find_youngest(people)
        new_list.append(youngest)
        people = remove_person_from_list(people, youngest)

    return new_list


# print(sort_people([{"name": "Jurgen", "age": 22}, {"name": "David", "age": 23}]))

# Home Work

def count(array, number):
    result = 0
    for n in array:
        if n == number:
            result = result + 1
    return result


def find_odd(numbers):
    for number in numbers:
        # appearnce = numbers.count(number)
        appearnce = count(numbers, number)
        if appearnce % 2 != 0:
            return number
    return None


def find_odd2(numbers):
    result = {}
    for number in numbers:
        if result.get(number) == None:
            result[number] = 1
        else:
            result[number] = result[number] + 1
    for key in result:
        if result[key] % 2 != 0:
            return key
    return None


# Home Work 2

def evenly_divisible(a, b, c):
    sum = 0
    for i in range(a, b + 1):
        if i % c == 0:
            sum = sum + i

    return sum

# print(evenly_divisible(1, 10, 2))


def find_all_odd(numbers):
    new_list = []
    for number in numbers:
        if number % 2 != 0:
            new_list.append(number)

    return new_list


# print(find_all_odd([1, 4, 2, 5]))

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

# print(count_numbers([1,1,2,2,4,6,10], [1, 10]))


def count_numbers2(numbers, target):
    newObj = {}
    for i in target:
        count = numbers.count(i)
        newObj[i] = count
    return newObj


# print(count_numbers2([1, 1, 2, 2, 4, 6, 10], [1, 10]))

# numbers = [1,1,2,2,4,6,10]
# numbers.count() #works only on arrays thats why is called method

# Home Work


def filter_list(list):
    just_int = []
    for i in list:
        if type(i) == int:
            just_int.append(i)

    return just_int

# print(filter_list([1, "a", "b", 0, 15]))


def XO(a):
    newObj = {}
    for i in a:
        count = a.count(i)
        newObj[i] = count
        if newObj[i] == newObj[i + 1]:
            return True
    else:
        return False

# print(XO("ooxx"))


def XO(a):
    newObj = {}
    for i in a:
        if newObj.get(i) == None:
            newObj[i] = 1
        else:
            newObj[i] = newObj[i] + 1
    print(newObj)
    if newObj.get("o") == newObj.get("x"):
        return True
    return False

# print(XO("zpzpzpzp"))


def XO2(a):
    count_x = 0
    count_o = 0
    for i in a:
        if i == "x":
            count_x += 1
        if i == "o":
            count_o += 1
    if count_x == count_o:
        return True

    return False

# print(XO2("xxo"))


def XO3(a):
    x = a.count("x")
    o = a.count("o")
    if x == o:
        return True
    return False

# print(XO3("xxoo"))

    # sorted_list = numbers.sort()      #Doesnt return a new array
    sorted_list = sort(numbers)        # Returns a new array
    # print(sorted_list)


def missing_num(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return 55 - sum

# print(missing_num([7, 2, 3, 6, 10, 9, 1, 4, 8]))


def reverse(a):
    reverse_string = ""
    position = len(a) - 1
    for i in range(len(a)):
        reverse_string = reverse_string + a[position]
        position = position - 1

    return reverse_string

# print(reverse("Hello World"))


def reverse2(a):
    reverse_string = ""
    for i in range(len(a)):
        reverse_string = reverse_string + a[len(a) - i - 1]

    return reverse_string

# print(reverse2("Hello World"))


# Write a function the takes 2 lists and return true if both lists have the same values otherwise return false.


def is_valid_PIN(a):
    if len(a) != 4 and len(a) != 6:
        return False
    else:
        for i in a:
            # print(i, type(i))
            if not i.isdigit():
                return False
    return True


# print(is_valid_PIN("12345"))

def is_valid_PIN(a):
    if len(a) != 4 and len(a) != 6:
        return False
    else:
        return a.isdigit()


# print(is_valid_PIN("1234"))

def same_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

# print(same_lists([1,2,3,4,5], [1,2,3,4]))


def same_lists2(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in list1:
        if i not in list2:
            return False
    return True

# print(same_lists2([1,4,3,2], [1,2,3,4]))


def same_lists3(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in list1:
        if list1.count(i) != list2.count(i):
            return False
    return True

# print(same_lists3([1,1,3,2], [1,2,3,1]))


def same_lists4(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

# print(same_lists4([1,3,4,2], [1,2,3,4]))


def same_lists5(list1, list2):
    if len(list1) != len(list2):
        return False
    numbers1 = sorted(list1)
    numbers2 = sorted(list2)
    for i in range(len(list1)):
        if numbers1[i] != numbers2[i]:
            return False
    return True

# print(same_lists5([1,2,1,3], [1,1,2,3]))


def setify(lst):  # transform into a List with no dublicates
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return sorted(new_list)

# print(setify([1, 5, 3, 5, 2]))


def is_symetrical(number):  # ornek
    num_to_string = str(number)
    print(num_to_string)
    if len(num_to_string) % 2 != 0:
        return False
    else:
        half_num1 = len(num_to_string) // 2
        first_half = num_to_string[:half_num1]
        second_half = num_to_string[half_num1:]
        print(first_half)
        print(second_half)
        for i in range(len(first_half)):
            if first_half[i] != second_half[len(second_half) - i - 1]:
                return False

    return True
# print(is_symetrical(7227))


def reverse_string(string):
    new_string = ""
    length = len(string)
    for i in range(length):
        new_string += string[length - i - 1]
    return new_string


def sym(number):
    str_number = str(number)
    reversed_str = reverse_string(str_number)
    return str_number == reversed_str


def sym(number):
    str_number = str(number)
    length = len(str_number)
    for i in range(length):
        if str_number[i] != str_number[length - i - 1]:
            return False
    return True
# print(sym(7227))


def reverse_list(number):
    new_list = []
    for i in range(len(number)):
        last_number = number[len(number) - i - 1]
        new_list.append(last_number)

    return new_list

# print(reverse_list([1, 2, 3, 4]))


def copy_half(lst):
    new_list = []
    half = len(lst) // 2
    for i in range(half):
        last_num = lst[len(lst) - i - 1]
        new_list.append(last_num)

    return new_list

# print(copy_half([1, 2, 3, 4]))


def copy_backward(lst1, lst2):
    new_list = []
    for i in range(len(lst1)):
        last_num = lst1[len(lst1) - i - 1]
        new_list.append(last_num)

    for y in range(len(lst2)):
        last_num2 = lst2[len(lst2) - y - 1]
        print(last_num2)
        new_list.append(last_num2)

    return new_list

# print(copy_backward([1, 2, 3, 4], [5, 6, 7, 8, 9]))


def halve_count(a, b):
    count = 0
    while a > b:
        a = a / 2
        count += 1

    return count - 1

# print(halve_count(624, 8))


# SORT BY LENGTH

def find_shortest_word(lst):
    shortest_word = lst[0]
    for word in lst:
        if len(word) < len(shortest_word):
            shortest_word = word

    return shortest_word


def remove_word_from_list(lst, word):
    new_words_list = []
    for i in lst:
        if i != word:
            new_words_list.append(i)

    return new_words_list


def sort_by_length(lst):
    sorted_length_list = []
    for i in lst:
        shortest = find_shortest_word(lst)
        sorted_length_list.append(shortest)
        lst = remove_word_from_list(lst, shortest)

    return sorted_length_list

# print(sort_by_length(["Google", "Apple", "Microsoft"]))


def cap_to_front(name):
    new_word = ""
    for i in name:
        if i.isupper():
            new_word = new_word + i
            # new_word.format(i)
    for i in name:
        if i.islower():
            new_word = new_word + i
            # new_word.format(i)
    return new_word

# print(cap_to_front("hApPy"))


def cap_to_front2(name):
    upper_case = ""
    lower_case = ""
    for i in name:
        if i.isupper():
            upper_case = upper_case + i
        if i.islower():
            lower_case = lower_case + i
    return upper_case + lower_case

# print(cap_to_front2("hApPy"))

# ef shh(phrase):
# ...     first_letter = phrase[0].upper()
# ...     rest = phrase[1:len(phrase)].lower()
# ...     return '"{}{}",  whispered Edabit.'.format(first_letter, rest)
# or return '"' + first_letter + rest + '" whispered Edabit.'


def letters_only(name):
    alphabet = "abcdefghijklmnopqrstuvxyz"
    new_string = ""
    for i in name:
        if i.lower() in alphabet:
            new_string += i
    return new_string

# print(letters_only("R!=:0o0./c%&k~60=y"))


def letters_only(name):
    new_string = ""
    for i in name:
        if i.isalpha():
            new_string += i
    return new_string

# print(letters_only("R!=:0o0./c%&k~60=y"))


def equal(lst):
    max_element = 0
    for i in lst:
        count = lst.count(i)
        if count > max_element:
            max_element = count
    if max_element == 1:
        return 0
    return max_element

# print(equal([3, 2, 3, 2, 1, 3, 3]))


def equal2(a, b, c):

    if a == b and a == c:
        return 3
    if a == b and a != c:
        return 2
    if a == c and a != b:
        return 2
    else:
        return 0

# print(equal2(2, 2, 2))


def find_sum(lst, number):
    sum = 0
    for i in lst:
        if lst[i] + lst[i + 1]:
            pass
# print(find_sum([1,2,4,5,7], 11))


def find_sum(lst, number):
    sum = 0
    for i in range(len(lst)):
        target = number - lst[i]
        if target in lst and lst:
            return [i, target]

    return None

# print(find_sum([1,2,5,6,7], 2))  #edge case = happens sometimes only when you pass specific arguments


def sum_to(numbers, num):
    for i in range(len(numbers)):
        target = num - numbers[i]
        if target in numbers and numbers.index(target) != i:
            return [numbers[i], target]
    return None
# print(sum_to([1,2,4,5], 2))

# With two functions


def find_target(numbers, target, index):
    for i in range(len(numbers)):
        if i != index and target == numbers[i]:
            return True
    return False


def sum_to(numbers, num):
    for i in range(len(numbers)):
        target = num - numbers[i]
        if find_target(numbers, target, i):
            return [numbers[i], target]
    return None


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Bazz"
    else:
        return "Not a multiple of 3 and 5 or not a number"

# print(fizz_buzz(35))


def number_length(num):
    num = str(num)
    count = 0
    for i in num:
        count += 1

    return count

# print(number_length(1234))


def invert(obj):
    new_obj = {}
    for i in obj:
        value = obj[i]
        new_obj[value] = i

    return new_obj

# print(invert({ "z": "q", "w": "f" }))


def find_missing(lst):
    for i in range(len(lst)):
        if i != lst[i]:
            return i
    return None
# print(find_missing([0, 1, 2, 3, 4, 5, 6, 7, 8]))


def fnd_miss(lst):
    start = lst[0]
    end = 0
    while end < len(lst):
        if start != lst[end]:
            return start
        start += 1
        end += 1
    return -1


def fnd_miss2(lst):
    idx = 0
    start = lst[0]
    length = len(lst)
    for i in range(start, start + length):
        if i != lst[idx]:
            return i
        idx += 1
    return -1


def fnd_miss3(lst):
    lst.sort()
    first = lst[0]
    length = len(lst)
    counter = 0
    total = sum(lst)
    for i in range(first, first + length+1):
        counter += i
    return counter - total
# print(fnd_miss3([21,20,24,23]))


def is_harshad(num):
    sum = 0
    string = str(num)
    for i in string:
        integer = int(i)
        sum += integer

    return num % sum == 0

# print(is_harshad(171))


def is_harshad2(lst):
    for i in lst:
        if is_harshad(i) != True:
            return False
    return True

# print(is_harshad2([12, 21, 24]))


def is_harshad(num):
    sum = 0
    string = str(num)
    for i in string:
        integer = int(i)
        sum += integer

    return num % sum == 0

# print(is_harshad(171))


def is_harshad2(lst):
    for i in lst:
        if not is_harshad(i):
            return False
    return True

# print(is_harshad2([12, 21, 24]))


def sum_odd_and_even(lst):
    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return [even_sum, odd_sum]

# print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))


def remove_duplicate(string):
    new_string = ""
    for i in string:
        if i.lower() not in new_string:
            new_string += i

    return new_string


def shared_letters(str1, str2):
    str1_new = remove_duplicate(str1)
    str2_new = remove_duplicate(str2)
    count = 0
    for i in str1_new:
        for y in str2_new:
            if i.lower() == y.lower():
                count += 1

    return count

# print(shared_letters("Apple", "meatyp"))


def shared_letters(str1, str2):
    new_lst = []
    for letter in str1:
        new_letter = letter.lower()
        if new_letter in str2.lower():
            if new_letter not in new_lst:
                new_lst.append(new_letter)

    return len(new_lst)
# print(shared_letters("Appppppple", "meatypp"))


def expensive_orders(orders, cost):
    higher_price = {}
    for i in orders:
        if orders[i] > cost:
            # higher_price.update({i: orders[i]})
            higher_price[i] = orders[i]  # key = value

    return higher_price

# print(expensive_orders({"a": 3000, "b": 200, "c": 1050}, 1000))


def sum_fractions(lst):
    sum = 0
    for i in range(len(lst)):
        fraction = round(lst[i][0] / lst[i][1])
        sum += fraction

    return sum

# print(sum_fractions([[18, 13], [4, 5]]))


def sum_fractions_2(lst):
    sum = 0
    for i in lst:
        fraction = round(i[0] / i[1])
        sum += fraction

    return sum

# print(sum_fractions_2([[36, 4], [22, 60]]))


def sum_fractions_3(lst):
    new_lst = []
    for i in lst:
        sum = 0
        for y in i:
            sum = sum + y
        new_lst.append(sum)

    return new_lst

# print(sum_fractions_3([[36, 4, 1], [22, 60]]))


def find_odd(lst):
    newObj = {}
    for i in lst:
        if newObj.get(i):
            newObj[i] = newObj[i] + 1
        else:
            newObj[i] = 1
    for key in newObj:
        if newObj[key] % 2 != 0:
            return key
    return None


# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))


def find_odd2(lst):
    for i in lst:
        count = lst.count(i)
        if count % 2 != 0:
            return i


# print(find_odd2([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))


def name_shuffle(str):
    lst = str.split(" ")
    new_txt = lst[1] + " " + lst[0]
    return new_txt


# print(name_shuffle("Donald Trump"))


def name_shuffle2(str):
    first_name = ""
    last_name = ""
    flag = False
    for i in str:
        if i == " ":
            flag = True
            continue
        if flag == True:
            last_name = last_name + i
        else:
            first_name = first_name + i
    return last_name + " " + first_name


# print(name_shuffle2("Donald Trump"))


def move_to_end(lst, num):
    new_lst = []
    for i in lst:
        if i != num:
            new_lst.append(i)
    for i in lst:
        if i == num:
            new_lst.append(i)

    return new_lst


# print(move_to_end([1, 3, 2, 4, 4, 1], 1))


def move_to_end2(lst, num):
    new_lst = []
    counter = 0
    for i in lst:
        if i == num:
            counter += 1
        else:
            new_lst.append(i)
    for i in range(counter):
        new_lst.append(num)


# print(move_to_end2([1, 3, 2, 4, 4, 1], 1))


def count_characters(lst):
    count_char = 0
    for i in lst:
        characters = len(i)
        count_char = count_char + characters

    return count_char


# print(count_characters(["###", "###", "###"]))

def xo(str):
    count_x = 0
    count_o = 0
    for i in str:
        if i.lower() == "x":
            count_x += 1
        elif i.lower() == "o":
            count_o += 1
    if count_x == count_o:
        return True
    else:
        return False


# print(xo("ooxXk"))


def xo1(str):
    count_x = 0
    count_o = 0
    for i in str:
        if i.lower() == "x":
            count_x += 1
        elif i.lower() == "o":
            count_o += 1
    return count_x == count_o


# print(xo1("ooxxx"))


def reverse(str):
    new_str = str[::-1]
    return new_str


# print(reverse("Hello World"))


def reverse(str):
    new_str = ""
    l = len(str)
    for i in range(l):
        last_letter = str[l - i - 1]
        if last_letter.isupper():
            new_str = new_str + last_letter.lower()
        else:
            new_str = new_str + last_letter.upper()

    return new_str


# print(reverse("jURGEN"))


def reverse2(str):
    l = len(str) - 1
    new_str = ""
    while l >= 0:
        last_letter = str[l]
        if last_letter.isupper():
            new_str = new_str + last_letter.lower()
        else:
            new_str = new_str + last_letter.upper()
        l = l - 1
    return new_str


# print(reverse2("jURGEN"))

def index_of_caps(str):
    lst = []
    for i in range(len(str)):
        if str[i].isupper():
            lst.append(i)

    return lst


# print(index_of_caps("eDaBiT"))


def is_isogram(str):
    new_obj = {}
    for i in str:
        letter = i.lower()
        if new_obj.get(letter):
            new_obj[letter] = new_obj[letter] + 1
        else:
            new_obj[letter] = 1
            print(new_obj)
    for i in new_obj:
        if new_obj[i] > 1:
            return False
    return True


# print(is_isogram("AlgorisSm"))


def is_isogram(str):
    for i in str:
        lower_letter = i.lower()
        upper_letter = i.upper()
        total = str.count(lower_letter) + str.count(upper_letter)
        if total > 1:
            return False
    return True


# print(is_isogram("AlgorisSm"))


def get_budgets(lst):
    sum = 0
    for i in range(len(lst)):
        lst_element = lst[i]
        sum += lst_element["budget"]
    return sum


# print(get_budgets([
#     {"name": "John", "age": 21, "budget": 23000},
#     {"name": "Steve",  "age": 32, "budget": 40000},
#     {"name": "Martin",  "age": 16, "budget": 2700}]))


def get_budgets(lst):
    sum = 0
    for element in lst:
        sum += element["budget"]
    return sum


# print(get_budgets([
#     {"name": "John", "age": 21, "budget": 23000},
#     {"name": "Steve",  "age": 32, "budget": 40000},
#     {"name": "Martin",  "age": 16, "budget": 2700}]))


def get_budgets(lst):
    for i in range(len(lst)):
        lst_element = lst[i]
        total = sum(lst_element["budget"])
    return total


# print(get_budgets([
#     {"name": "John", "age": 21, "budget": 23000},
#     {"name": "Steve",  "age": 32, "budget": 40000},
#     {"name": "Martin",  "age": 16, "budget": 2700}
# ]))

lst = [10, 20, 10, 30, 20, 11]


def dublicate_num(lst):
    for i in range(len(lst)):
        for y in range(len(lst)):
            if i == y:
                continue
            if lst[i] == lst[y]:
                return True
    return False


def find_largest_number(lst):
    largest_number = lst[0]
    # largest_number = 0
    for num in lst:
        if num > largest_number:
            largest_number = num

    return largest_number


# print(find_largest_number([-4, -5, -6, -1, -3]))


def reverse(lst):
    r = lst.reverse()
    return r


# print(reverse([1, 2, 3, 4]))


def reverse(lst):
    new_lst = []
    l = len(lst)
    for i in range(l):
        last_letter = lst[l-i-1]
        new_lst.append(last_letter)

    return new_lst


# print(reverse([1, 2, 3, 4]))


def do_math(str):
    new_str = str.split(" ")
    a = new_str[0]
    b = new_str[2]
    c = new_str[4]
    print(new_str)
    if new_str[1] == "+":
        return int(a) + int(b)
    elif new_str[1] == "-":
        return int(a) - int(b)


# print(do_math("45 + 1"))


def do_math(str):
    a = ""
    b = ""
    operation = ""
    for i in str:
        if i == " ":
            continue
        if i == "+" or i == "-":
            operation = i
            continue

        if operation in ("+", "-"):
            b += i
        else:
            a += i

    if operation == "+":
        return int(a) + int(b)
    elif operation == "-":
        return int(a) - int(b)


# print(do_math("1 + 2"))


def do_math(str):
    new_str = str.split(" ")
    print(new_str)
    sum1 = 0
    sum2 = 0
    a = new_str[0]
    b = new_str[2]
    c = new_str[4]
    if new_str[1] == "+":
        sum1 = int(a) + int(b)
    elif new_str[1] == "-":
        sum1 = int(a) - int(b)

    if new_str[3] == "+":
        sum2 = sum1 + int(c)
    elif new_str[3] == "-":
        sum2 = sum1 - int(c)

    return sum2


# sprint(do_math("1 + 100 - 44"))

def do_math5(expression):
    n_lst = expression.split()
    total = 0
    sign = None
    for n in n_lst:
        if sign != None:
            if sign == "-":
                total = total - int(n)
            else:
                total = total + int(n)
            sign = None

        elif n.isdigit():
            total = int(n)
        else:
            sign = n
    return total


# print(do_math5("1 + 100 - 44 + 10"))


class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        for i in range(len(number) // 2):
            if number[i] != number[len(number) - i - 1]:
                return False

        return True


def mergeTwoLists(l1, l2):
    new_list = []
    for i in range(len(l1)):
        if l1[i] < l2[i]:
            new_list.append(l1[i])
            new_list.append(l2[i])
        elif l1[i] > l2[i]:
            new_list.append(l2[i])
            new_list.append(l1[i])
        else:
            new_list.append(l1[i])
            new_list.append(l2[i])

    return new_list


# print(mergeTwoLists([1, 2, 4], [1, 3, 4]))


class Person:
    def __init__(self, name, lastname, age):  # self is the object
        self.name = name
        self.lastname = lastname
        self.age = age

    def say_name(self, height):  # method
        print(self.name, self.lastname, height)

    def info(self):
        print(self.name)
        print(self.lastname)
        print(self.age)

    def is_name(self, name):
        if self.name == name:
            return True
        return False

        # class creates an object with these qualities
person1 = Person("John", "Nick", 24)
person2 = Person("Peter", "Dickson", 23)
# print(person1.name)
# print(person2.name)
# create a new height method if you want to print just name or the lastname
# person1.say_name(180)
# person2.say_name(175)
# person2.info()
# person1.info()
# print(person1.is_name("John"))


class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiplay(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


calculator = Calculator()

# print(calculator.add(2, 3))
# print(calculator.subtract(2, 3))
# print(calculator.multiplay(2, 3))
# print(calculator.divide(2, 3))


class Employe:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.email = f"{firstname.lower()}.{lastname.lower()}@company.com"


emp_1 = Employe("John", "Smith")
# print(emp_1.fullname)
# print(emp_1.email)


class Player:
    def __init__(self, name, age, height, weight):  # constractor
        self.name = name  # instant attributes
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):  # methods
        return self.name + " is age " + str(self.age)

    def get_height(self):
        return self.name + " is " + str(self.height) + "cm"

    def get_weight(self):
        return self.name + " is weighs " + str(self.weight) + "kg"


player1 = Player("Christiano Ronaldo", 36, 182, 73)
# print(player1.get_age())
# print(player1.get_height())
# print(player1.get_weight())


def to_list(dict):
    main_lst = []
    for i in dict:
        second_lst = []
        second_lst.append(i)
        value = dict[i]
        second_lst.append(value)
        main_lst.append(second_lst)

    return main_lst


#print(to_list({"a": 1, "b": 2}))


def to_list(dict):
    main_lst = []
    for i in dict:
        value = dict[i]
        second_lst = [i, value]
        main_lst.append(second_lst)

    return main_lst


print(to_list({"a": 1, "b": 2}))
