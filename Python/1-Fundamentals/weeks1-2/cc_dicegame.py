import random

high_score = 0


def dice_game():

    global high_score

    while True:

        print("\nCurrent High Score", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            roll_1 = random.randint(1, 6)
            print("You roll...", roll_1)
            roll_2 = random.randint(1, 6)
            print("You roll...", roll_2)
            total = roll_1 + roll_2
            print("You have rolled a total of:", total)
            if total > high_score:
                high_score = total
                print("New highscore")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


dice_game()
