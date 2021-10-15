class User:  # class
    def __init__(self, name, email, password):  # constructor method
        self.name = name                        # instance attributes
        self.email = email
        self.password = password

    def change_password(self, password):  # instance method
        self.password = password
        print("Your password has been changed to", self.password)


user1 = User("jane", "jane@nucamp.co", "janepassword")
print(user1.password)

user1.change_password("bestpassword")
