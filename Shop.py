def shopping(coins):    
    print ("'Welcome, young adventurer!' the sealler says, approaching slowly.' I'd be happy to assist you.'\nYou look over the available weapons:\n\n  1.Simple Steel Sword - 50 gold coins: A balanced and easy-to-handle sword. Ideal for a novice adventurer.\n  2. Hand Axe - 70 gold coins: A compact and powerful axe, perfect for cutting both wood and enemies.\n  3. Short Wooden Bow - 65 gold coins: A simple yet effective bow for those who prefer ranged attacks.\n  4. Silver Dagger - 45 gold coins: A small, lightweight, and sharp dagger, good for quick and discreet combat\n  5. Iron Mace - 60 gold coins: A heavy mace capable of dealing significant damage to enemies.\n\n")
    while True:
        desition = int(input("After considering your options and the amount of gold you have, you decide to buy... ")) 
        weapon= ""
        if desition == 1:
            weapon = "Simple Steel Sword"
            coins -= 50
            breakpoint
        elif desition == 2:
            weapon = "Hand Axe"
            coins -= 70
            break
        elif desition == 3:
            weapon = "Short Wooden Bow"
            coins -= 65
            break
        elif desition == 4:
            weapon = "Silver Dagger"
            coins -= 45
            break
        elif desition == 5:
            weapon = "Iron Mace"
            coins -= 60
            break
        else: 
            print("Invalid choise")
            continue
    return weapon, coins
