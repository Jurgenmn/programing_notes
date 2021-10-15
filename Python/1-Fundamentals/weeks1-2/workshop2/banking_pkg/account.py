def show_balance(balance):
    print("You balance is: $", balance)


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + int(amount)


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return balance - int(amount)


def logout(name):
    print("Goodbye", name)
