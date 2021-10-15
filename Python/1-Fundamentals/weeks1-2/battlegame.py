wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:

    print("Wizard")
    print("Elf")
    print("Human")
    character = input("Choose your charachter: ")

    if character == "1":
        character = wizard
        print("You have choosen the character: " + wizard)
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    if character == "2":
        print("You have choosen the character: " + elf)
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    if character == "3":
        print("You have choosen the character: " + human)
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    else:
        print("Unknown character, type 1, 2 or 3")

while True:
    dragon_hp = dragon_hp - my_damage
    print(my_damage)
    print("The", character, "damged the Dragon!")
    print("The Dragon's hitpoints are now", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character, "'s hitpoints are now", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle!")
        break
