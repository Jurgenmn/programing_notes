# from donations_pkg import homepage
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""


while True:

    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    option = input("Choose an option ")
    if option == "1":
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = login(database, user_name, password)
    elif option == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    elif option == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print("""Leaving DonateME...
    Goodbye!""")
        break
