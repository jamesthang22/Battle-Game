# task 1
wizard = "Wizard"
elf = "Elf"
human = "Human"
jamesT = "Dr. Thang"
dragon = "Dragon"

wizard_hp = 70
elf_hp = 100
human_hp = 150
james_hp = 1000
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
jamesT_damage = 200
dragon_damage = 50

# task 2
while True:
    choice = input("p for PLAY, q for QUIT: ").upper()
    print("")
    if choice == "P":

        while True:
            print("1) Wizard")
            print("2) Elf")
            print("3) Human")
            print("4) JamesT")
            user = input("Choose your charater: ").upper()
            # task 3
            if user == "1" or user == "WIZARD":
                character = wizard
                my_hp = wizard_hp
                my_damage = wizard_damage
                break
            if user == "2" or user == "ELF":
                character = elf
                my_hp = elf_hp
                my_damage = elf_damage
                break
            if user == "3" or user == "HUMAN":
                character = human
                my_hp = human_hp
                my_damage = human_damage
                break
            if user == "4" or user == "JAMEST":
                character = jamesT
                my_hp = james_hp
                my_damage = james_hp
                break
            else:
                print("Unknown Charater")
                break
        # task 3
        print("You've chosen the character: " + character)
        print("Health ", + my_hp)
        print("Damage ", + my_damage, "\n")

        # task 4
        while True:
            dragon_hp -= my_damage
            print("The", character, "damaged the Dragon!")
            print("The Dragaon hitpoints are not: ", + dragon_hp, "\n")

            if dragon_hp <= 0:
                print("The Dragon has lost the battle")
                break
            my_hp -= dragon_damage
            print("The Dragon strakes back at" + character)
            print("The " + character + "'s hitpoints are now ", + my_hp, "\n")

            if my_hp <= 0:
                print(character + " has lots the battle")
                break

    if choice == "Q":
        print("Good Bye!")
        break
