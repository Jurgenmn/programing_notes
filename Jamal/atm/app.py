class User:
    def __init__(self, first_name, last_name, user_name, password, id):
        self.fname = first_name
        self.lname = last_name
        self.username = user_name
        self.password = password
        self.balance = 0
        self.id = id

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def send(self, user, amount):
        self.balance = self.balance - amount  # withdrawing from the sender's account
        user.balance = user.balance + amount  # Adding to to recivers account

    def request(self, user, amount):
        user.balance = user.balance - amount
        self.balance = self.balance + amount


def interface():

    print("-------------------------------------")
    print("1)  Login      |    2)  Sign up      ")
    print("-------------------------------------")
    print("3)  Deposit    |    4)  Withdraw     ")
    print("-------------------------------------")
    print("5)  Send       |    6)  Request      ")
    print("-------------------------------------")
    print("7)  Logout     |    8)  Exit        ")


def find_user(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None


def find_user_by_id(users, id):
    for user in users:
        if user.id == id:
            return user
    return None


user_id = 1


test_user = User("Jurgen", "Mane", "Jurgen1", "1234", 0)
users = [test_user]

is_loged_in = False
current_user = None

while True:
    interface()
    if is_loged_in == True:
        print("Logged in user: " + current_user.fname + " " +
              current_user.lname + " with the balance: " + str(current_user.balance) + "\n")

    option = input(">: ")

    if option == "1":
        username = input("Username: ")
        password = input("Password: ")
        user = find_user(users, username, password)
        if user != None:
            is_loged_in = True
            current_user = user
        else:
            print("Invalid information")

    elif option == "2":
        fname = input("First name: ")
        lname = input("Last name: ")
        username = input("Username: ")
        password = input("Password: ")

        user = User(fname, lname, username, password, user_id)
        user_id += 1
        users.append(user)
        is_loged_in = True
        current_user = user

    elif option == "3":
        if is_loged_in == True:
            new_deposit = int(input("Amount: "))
            current_user.deposit(new_deposit)
        else:
            print("Please log in first")
            continue

    elif option == "4":
        if is_loged_in == True:
            new_withdraw = int(input("Amount: "))
            current_user.withdraw(new_withdraw)
        else:
            print("Please log in first")

    elif option == "5":
        if is_loged_in == True:
            reciver_id = int(input("User id: "))
            send_amn = int(input("Amount: "))
            user = find_user_by_id(users, reciver_id)
            if user == None:
                print("Reciver not found")
            else:
                current_user.send(user, send_amn)
        else:
            print("Please login")

    elif option == "6":
        if is_loged_in == True:
            sender_id = int(input("Sender ID: "))
            receive_amn = int(input("How much money do you want to request: "))
            sender = find_user_by_id(users, sender_id)
            if sender == None:
                print("Sender not found")
            else:
                current_user.request(sender, receive_amn)
        else:
            print("Please log in")

    elif option == "7":
        is_loged_in = False
        current_user = None

    elif option == "8":
        print("Goodbye!!")
        break
