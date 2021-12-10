def count_names(names):
    newObj = {}
    for name in names:
        if newObj.get(name):
            newObj[name] = newObj[name] + 1
        else:
            newObj[name] = 1
    return newObj


print(count_names(["Jurgen", "Matthew", "Jurgen",
      "John", "David", "Matthew", "Matthew", "John"]))


def invert(obj):
    new_obj = {}
    for i in obj:
        value = obj[i]
        new_obj[value] = i

    return new_obj

#print(invert({ "z": "q", "w": "f" }))


def reverse(name):
    new_name = ""
    for i in range(len(name)):
        new_name = new_name + name[len(name) - i - 1]

    return new_name

# print(reverse("Jamal"))


def shared_letters(str1, str2):
    count = 0
    for i in str1:
        if i in str2:
            count += 1
    return count
#print(shared_letters("Apple", "meaty"))
