class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def print_info(self):
        print(self.name, self.age, self.type)


class Dog(Animal):
    def __init__(self, name, age, type, owner, owner_nr):
        Animal.__init__(self, name, age, type)
        self.owner = owner
        self.owner_nr = owner_nr

    def print_info(self):
        Animal.print_info(self)
        print(self.owner, self.owner_nr)


dog = Dog("Hachi", 8, "dog", "Richard", 2244778455)


dog.print_info()


"""
animal = Animal(question1, question2, question3)
animal.print_info()



def interface():

    print("1) Search Animal")
    print("2) Create Animal")
    print("3) Exit")


def find_animal(animal_list, name, type):
    for animal in animal_list:
        if animal.name == name and animal.type == type:
            return animal
    return -1


animal_list = []

while True:
    interface()

    option = input("Choose option: ")
    if option == "2":
        print("Create the animal: ")
        question1 = input("Whats the name: ")
        question2 = input("Whats the age: ")
        question3 = input("Whats the type: ")
        animal = Animal(question1, question2, question3)
        animal_list.append(animal)

    elif option == "1":
        animal_name = input("What is the animal name: ")
        animal_type = input("What is the animal type: ")
        animal = find_animal(animal_list, animal_name, animal_type)
        if animal != -1:
            animal.print_info()
        else:
            print("Animal not in the list")

    elif option == "3":
        print("Goodbye!")
        break
"""
