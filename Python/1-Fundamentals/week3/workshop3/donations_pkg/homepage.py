def show_homepage():

    print("              === DonateME Homepage ===              ")
    print("-----------------------------------------------------")
    print("| 1.   Login             | 2.   Register            |")
    print("-----------------------------------------------------")
    print("| 3.   Donate            | 4.   Show Donations      |")
    print("-----------------------------------------------------")
    print("|                      5. Exit                      |")
    print("-----------------------------------------------------")


def donate(username):

    donation_amt = input("Enter amount to donate: ")
    donation_amt = float(donation_amt)
    donation = username + " donated " + str(donation_amt)
    print("Thank for donating")
    return donation


def show_donations(donations):
    print("\n----All Donations---")
    if len(donations) == 0:
        print("Currently, there are no donations")
    else:
        for donation in donations:
            print(donation)
