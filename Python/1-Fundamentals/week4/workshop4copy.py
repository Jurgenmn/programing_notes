
class User:
    def __init__(self, name, pin, password):
        self.name = name  # object is self and .name is the property
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of :", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def transfer_money(self, user):
        amount = int(input("Amount of transfer: "))
        print("You are transfering $", amount, "to", user.name)
        print("Authentication required")
        print("Enter your PIN")
        pin = input("PIN??: ")
        if pin == self.pin:
            print("Transfer authorized")
            print("Transfering $", amount, "to", user.name)
            user.balance = user.balance + amount
            self.balance = self.balance - amount
            return True
        else:
            print("Invalid PIN. Transaction canceled")
            return False

    def request_money(self, user):
        amount = int(input("Amount of request: "))
        print("You are requesting $", amount, "from", user.name)
        print("User uthentication required....")
        print("Enter " + user.name + "'s PIN")
        pin = input("PIN: ")
        if pin == user.pin:
            print("Enter your password")
            password = input("Password: ")
            if password == self.password:
                print("Request authorized")
                print(user.name, "sent $", amount)
                user.balance = user.balance - amount
                self.balance = self.balance + amount
                return True
            else:
                print("Invalid password. Transaction canceled")

        else:
            print("Invalid PIN. Transaction canceled")
            return False


'''
""" Driver Code for Task 1 """

user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """

user2 = User("Bob", 1234, "password")
print(user2.name, user2.pin, user2.password)


user2.change_name("Jurgen")
user2.change_pin(12345)
user2.change_password("Passssword")

print(user2.name, user2.pin, user2.password)


""" Driver Code for Task 3 """

bank_user = BankUser("Bob", "1234", "bankpassword")
print(bank_user.name, bank_user.pin, bank_user.password, bank_user.balance)

bank_user.name = "Jurgen"

bank_user.change_name("David")

print(bank_user.name)


""" Driver Code for Task 4 """

bank_user2 = BankUser("Bob", "1234", "bankpassword")
bank_user2.show_balance()
bank_user2.deposit(1000)
bank_user2.show_balance()
bank_user2.withdraw(250)
bank_user2.show_balance()
'''

""" Driver Code for Task 5 """

bank_user3 = BankUser("Bob", "1234", "bankpassword")
bank_user4 = BankUser("Alice", "5678", "password1234")

