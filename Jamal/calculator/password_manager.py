from random import randint


def display_menu():
    print("1: Lookup password")
    print("2: Create new account")
    print("3: Generate random password")
    print("-1: Exit the program")


def write_data(account_name, password):
    handler = open("passwords", "a")  # appending
    data = account_name + ":" + password + "\n"
    handler.write(data)

# write_data("Google", "1234")
# write_data("Facebook", "5678")


def read_data():
    handler = open("passwords", "r")
    data = handler.readlines()
    return data

# print(read_data())
# print("")
# print("")


def filter_password(account_name, lst_accounts):
    new_account_lst = []
    for account in lst_accounts:
        if account_name in account:
            new_account_lst.append(account[:-1])

    return new_account_lst

#print(filter_password("Google",['Google:1234\n', 'Facebook:5678\n', 'Google:1234\n', 'Gitthub:987654\n']))
# print("")
# print("")


accounts = {}

while True:

    display_menu()
    # print(accounts)

    action = input("What would you like to do? ")

    if action == "1":
        name = input("Account Name: ")
        # print("\n\n Password for " + name + " is " + accounts[name] + "\n\n")
        lines = read_data()
        passwords = filter_password(name, lines)
        print(passwords)
        print("")

    if action == "2":
        name = input("Account name: ")
        password = input("Password: ")
        # accounts[name] = password
        write_data(name, password)
    if action == "3":
        print(generate_random_password())
    if action == "-1":
        break
