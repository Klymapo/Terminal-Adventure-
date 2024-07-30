import random as RN

def What_are_you_gonna_do(INT, SPD):
    print("Right know, you have three options:\n  1. Try to talk wit them (INTELLIGENCE + DICE > 11)\n  2. Fight them directly\n   3. Run (SPEED + DICE > 18)")
    question = int(input("What are you going to do? 1,2 or 3"))
    if question == 1:
        achive = int(INT + RN.rendit(1,20))
        if achive >= 11:
            return "ACHIVEMET 1"
        else:
            return "FAIL 1"
    elif question == 2:
        return "FIGHT"
    elif question == 3:
        achive = int(SPD + RN.rendit(1,20))
        if achive >= 18:
            return "ACHIVEMET 1"
        else:
            return "FAIL 2"
def Fight(STRN, SPD, HP):
    num_kobolds = 3
    kobold_damage = [RN.randint(2, 5) for _ in range(num_kobolds)]  
    kobold_HP = [RN.randint(6, 10) for _ in range(num_kobolds)]  
    print(f"{num_kobolds} Kobolds approach you!")

    while num_kobolds > 0 and HP > 5:
        for kobold_index in range(num_kobolds):
            print(f"\nKobold {kobold_index + 1} lunges at you with a rusty knife. You try to parry his attack")
            parry = SPD + RN.randint(1, 20)
            ready_to_next = input("Tap ENTER to continue... ")

            if ready_to_next == "":
                next_step = True
            
            print(f"Your score (SPD + DICE) for this action is {parry}")
            if parry > 12:
                print(f"You made it!\nYou strike back at Kobold {kobold_index + 1}.")
                damage_to_kobold = STRN + RN.randint(1, 6)
                kobold_HP[kobold_index] -= damage_to_kobold
                print(f"You dealt {damage_to_kobold} damage to Kobold {kobold_index + 1}. Remaining HP of Kobold: {kobold_HP[kobold_index]}")
                if kobold_HP[kobold_index] <= 0:
                    print(f"You have defeated Kobold {kobold_index + 1}!")
                    num_kobolds -= 1
                    kobold_HP.pop(kobold_index)
                    kobold_damage.pop(kobold_index)
                    break
                print(f"Remaining Kobolds: {num_kobolds}")
            else:
                damage = kobold_damage[kobold_index]
                print(f"Kobold {kobold_index + 1} hit you. Oh no! It deals {damage} damage.")
                HP -= damage
                print(f"Now your HP is {HP}")
                if HP <= 4:
                    break
            
            if num_kobolds > 0:
                print("\nMore Kobolds approach, but you try to use a fallen branch to trip them.")
    
    if HP <= 4:
        print("\nYour HP is too low. You need to retreat!")
    else:
        print("\nYou have defeated all the Kobolds!")

    return HP, next_step

