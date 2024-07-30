import random as RN

def What_to_do(INT, SPD, choice):
    options = {
        1: (INT, 11, "ACHIEVEMENT", "FAIL"),
        3: (SPD, 18, "ACHIEVEMENT", "FAIL")
    }
    if choice in options:
        stat, threshold, success, failure = options[choice]
        achievement = stat + RN.randint(1, 20)
        return success if achievement >= threshold else failure
    elif choice == 2:
        return "FIGHT"
    else:
        return "Invalid choice"


def Fight(STRN, SPD, HP):
    num_kobolds = 3
    kobold_damage = [RN.randint(2, 5) for _ in range(num_kobolds)]
    kobold_HP = [RN.randint(6, 10) for _ in range(num_kobolds)]
    next_step = False
    
    results = []
    results.append(f"{num_kobolds} Kobolds approach you!")
    
    while num_kobolds > 0 and HP > 5:
        for kobold_index in range(num_kobolds):
            parry = SPD + RN.randint(1, 20)
            results.append(f"\nKobold {kobold_index + 1} lunges at you with a rusty knife. You try to parry his attack")
            results.append(f"Your score (SPD + DICE) for this action is {parry}")
            
            if parry > 12:
                damage_to_kobold = STRN + RN.randint(1, 6)
                kobold_HP[kobold_index] -= damage_to_kobold
                results.append(f"You made it! You strike back at Kobold {kobold_index + 1}.")
                results.append(f"You dealt {damage_to_kobold} damage to Kobold {kobold_index + 1}. Remaining HP of Kobold: {kobold_HP[kobold_index]}")
                if kobold_HP[kobold_index] <= 0:
                    results.append(f"You have defeated Kobold {kobold_index + 1}!")
                    num_kobolds -= 1
                    kobold_HP.pop(kobold_index)
                    kobold_damage.pop(kobold_index)
                    break
                results.append(f"Remaining Kobolds: {num_kobolds}")
            else:
                damage = kobold_damage[kobold_index]
                HP -= damage
                results.append(f"Kobold {kobold_index + 1} hit you. Oh no! It deals {damage} damage.")
                results.append(f"Now your HP is {HP}")
                if HP <= 4:
                    break
        
        if num_kobolds > 0 and HP > 4:
            results.append("\nMore Kobolds approach, but you try to use a fallen branch to trip them.")
    
    if HP <= 4:
        results.append("\nYour HP is too low. You need to retreat!")
    else:
        results.append("\nYou have defeated all the Kobolds!")
    
    return HP, next_step, results
