#------------------------------ KLYMAPO'S GAME ADEVENTURE ------------------------------
#--------------------------- Created on: Tuesday, November 5th, 2021 -------------------
import os
import platform
import Texts as TX
import Character_Creation as CC
import Shop as SP
import ALTERNATIVE1 as D1
#---------------------------------------------------------------------------------------
def NEXT():
    Next = False
    Readay_To_Next = input("Tap ENTER to continue... ")
    if Readay_To_Next == "":
        Next = True
        sistema = platform.system()
        if sistema == "Windows":
          os.system("cls")  
        else:
          os.system("clear")
    return Next
def Action_System_Explication():
   need_explication = input("\n \n Would you like to know what are tha stats for? (Y/N) ").upper()
   while True:
    if need_explication == "Y" or need_explication == "YES":
      print("All right, now we are going to explain how de interactios work\nBasically every time you make an action the game will request a minimum of points to decide if you can made the action or not.\nThe game system will roll a twenty faces dice.\nTo that score, the game is going to add your personal especific stat that is rellationed to that activity to achive.\nYou will have a multiple descition ask to make a diferent action, knowing your personal stats to decide what is easier for you to made")
      break
    else:
      return "Let´s continue then"
    
#--------------------------- INTRO -----------------------------------------------------
sistema = platform.system()
if sistema == "Windows":
  os.system("cls")  
else:
  os.system("clear")
print(TX.text1)
NEXT()
#--------------------------- CHARECTER CREATION ----------------------------------------
name = CC.Character_Name()
NEXT()
stats = list(CC.Character_Stats())
character = {"player" : name,
             "rol" : stats[0],
             "STR" : stats[1],
             "SPD" : stats[2],
             "INT" : stats[3],
             "HP" : stats[4]}
print(f"You are the mighty {character['player']} and as a {character['rol']} you stats are:\n {character['STR']} strenght\n {character['SPD']} speed\n {character['INT']} intelligence\n {character['HP']} HP")
Action_System_Explication()
NEXT()
print(TX.text2)
#--------------------------- SHOP ------------------------------------------------
print(TX.text3)
NEXT()
coins = 100
sell = list(SP.shopping(coins))
weapon = sell[0]
coins = sell[1]
print(f"'An excellent choice. May this {weapon} serve you well in your adventures'. You thank the sealler and leave the shop with your new {weapon}, ready to face the Shadow Forest.\nYou have {coins} left. ")
NEXT()

#--------------------------- KOBOLD MEETING ------------------------------------------------
print(TX.text4)
choice = int(input("Right know, you have three options:\n  1. Try to talk wit them (INTELLIGENCE + DICE > 11)\n  2. Fight them directly\n  3. Run (SPEED + DICE > 18)\n\n"))
action = D1.What_to_do(character["INT"], character["SPD"], choice)
if choice == 1:
  print("You try to talk with them. (THE DICE WILL ROLL)")
  print("You have a...")
  print(action)
  NEXT()
  if action == "ACHIEVEMENT":
    print(TX.text5)
    NEXT()
  else:
    print(TX.text6)
    NEXT()
    print(TX.batlle)
    NEXT()
elif choice == 2:
  print(TX.text7)
  NEXT()
  print(TX.batlle)
  NEXT()
else:
  print("You try to run (THE DICE WILL ROLL)")
  print("You have a...")
  print(action)
  NEXT()
  if action == "ACHIEVEMENT":
    print(TX.text8)
    NEXT()
  else:
    print(TX.text9)
    NEXT()
    print(TX.batlle)
    NEXT()
#--------------------------- FINISH KOBOLD FIGHT ------------------------------------------
print(TX.text10)
NEXT()
belive = str(input("\nDo you belived him?\n ").upper())
if belive == "Y":
  print(TX.text11)
  NEXT()
else:
  print(TX.text12)
  NEXT()

print("THE END")
