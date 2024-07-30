import os
import platform

def Character_Name():
    while True:  
        name = input("How should we call you? \n")
        q1 = input(f"\nYou are {name}. Is that correct? (Y/N) \n").upper()
        if q1 == "Y" or q1 == "YES":
            print(f"Very well {name}. Why do you don't pick a class? \n\n")
            return name
        else:
            print("Oh, I beg you pardon. Let´s try again")
def Character_Stats():
    class_type = ""
    streng = 8
    speed = 6
    intelligence = 6
    HP = 12

    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")  
    else:
        os.system("clear")
    
    print("You can be a valeurous adventurer being... \n\n")
    print("  1. Barbarian (+3 STRENG) (-2 SPEED) (+2 HP) (-2 INTELLIGENCE)\n ")
    print("  2. Wizard (+3 INTELLIGENCE) (-2 STRENG) (-1 HP)  \n ")
    print("  3. Rogue (+1 INTELLIGENCE) (+2 SPEED) (-1 STRENG) \n ")
    print("  4. Shooter (+1 STRENG) (+3 SPEED) (+1 INTELLIGENCE) (-2 HP) \n")

    picking = True
    while picking:
        chosing = True
        while chosing:
            class_choice = int(input("Enter the number of your class: \n"))
            if class_choice < 5:
                if class_choice == 1:
                    class_type = "Barbarian"
                    streng += 3
                    speed -= 2
                    intelligence -= 2
                    HP += 2
                    chosing = False
                elif class_choice == 2:
                    class_type = "Wizard"
                    streng -= 2
                    intelligence += 3
                    HP -= 1
                    chosing = False
                elif class_choice == 3:
                    class_type = "Rogue"
                    streng -= 1
                    intelligence += 1
                    speed += 2
                    chosing = False
                elif class_choice == 4:
                    class_type = "Shooter"
                    streng += 1
                    speed += 3
                    intelligence += 1
                    HP -= 2
                    chosing = False
            else:
                print("Invalid choice. Please choose a valid class.")
                continue
        print(f"Class: {class_type}, Streng: {streng}, Speed: {speed}, Intelligence: {intelligence}, HP: {HP} ")
        q2 = input("Wanna change your class? (Y/N) \n").upper()
        if q2 == "Y":
            continue
        else:
            return class_type, streng, speed, intelligence, HP

        