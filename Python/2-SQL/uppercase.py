word = "HeLlo wOrLD"


def reverse_letters(word):
    new_word = ""
    for i in word:
        if i.isupper():
            new_word = new_word + i.lower()
        else:
            new_word = new_word + i.upper()

    return new_word


print(reverse_letters(word))
