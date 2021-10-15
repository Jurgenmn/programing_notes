import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    print(" ")
    print("----------- START GAME -------------")
    print(" ")
    while tries != 0:
        print("Numbers of tries left: ", tries)
        guess = int(input("Guess a number between " +
                    str(start) + " and " + str(stop) + ": "))
        print(" ")
        if guess == random_number:
            print("Good job, you guessed the correct number")
            print("You deserve a kissss..")
            break
        elif guess < random_number and guess >= start:
            print("Your guess is lower than random number")
            print(" ")
            print("--------------------------------------")
        elif guess > random_number and guess <= stop:
            print("Your guess is higher than the random number")
            print(" ")
            print("-------------------------------------------")
        else:
            print("Guess out of range")
        tries -= 1
        if tries == 0:
            print("You loser, you failed to guess the number: ", random_number)
            print(" ")
            print("------------ GAME OVER -----------")
            break


def guess_random_number_num_linear(tries, start, stop):  # linear search
    random_number = random.randint(start, stop)
    print("The number for the program to guess is:", random_number)
    for i in range(start, stop):
        print("The program is guessing...", i)
        print("Number of guessies left", tries)
        if i == random_number:
            print("You guessed the correct number", random_number)
            return True
        tries -= 1
        if tries == 0:
            print("You didnt guess the number", random_number)
            return


#guess_random_number_num_linear(7, 1, 15)


def guess_random_num_binary(tries, start, stop):  # binary search
    random_number = random.randint(start, stop)
    print("Random number to find: ", random_number)
    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
        middle_point = (lower_bound + upper_bound) // 2
        #print("Your guess is: ", middle_point)
        if random_number == middle_point:
            print("You guessed the correct number", random_number)
            break
        elif middle_point < random_number:
            print("Guessing lower")
            lower_bound = middle_point + 1
        elif middle_point > random_number:
            print("Guessing higher")
            upper_bound = middle_point - 1
        tries -= 1
        if tries == 0:
            print("Your program failed to find the number", random_number)
            break


#guess_random_num_binary(6, 1, 100)

while True:
    guess_random_number(5, 1, 100)
