import random

#Starting Balance
global money
money = 100

#Introduction
print("Welcome to Stevie's Casino!")
print("Here are some credits to get you started!")
print("Credits: " + str(money))

#Write your game of chance functions here

#Coin Toss (Pick "Heads" or "Tails")
def coin_toss(call, bet):
  global money
  print("COIN TOSS!")
  if call == "Heads":
    print ("You chose Heads!")
    myNum = 1
  elif call == "Tails":
    print ("You chose Tails!")
    myNum = 2
  num = random.randint(1,2)
  if num == 1:
    print("The coin landed on Heads!")
  else:
    print("The coin landed on Tails!")
  if num == myNum :
    print("You got it!")
    print("You won "+ str(bet))
    money += bet
    print("Credits: " + str(money))
    return
  else:
    print("You lost " + str(bet))
    money -= bet
    print("Credits: " + str(money))
    return
    
#Cho Han - Roll two dice, choose whether the sum will be Odd or Even (0 for Even, 1 for Odd).
def cho_han(call, bet):
  global money
  print("Lets Play Cho-Han!")
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  dice = dice1 + dice2
  print("You rolled a " + str(dice1) + " and a " + str(dice2) + ", totaling " + str(dice))
  if call == "Even": 
    print("You picked Even!")
    if dice % 2 == 0:
      print("You were right!")
      money += bet
      print("You won: " + str(bet))
    elif dice % 2 == 1:
      print("The total is odd.")
      money -= bet
      print("You lost: "+ str(bet))
  elif call == "Odd":
    print ("You picked Odd!")
    if dice % 2 == 1:
      print("You were right!")
      money += bet
      print("You won " + str(bet))
    elif dice % 2 == 0:
      print("The total is even.")
      money -= bet
      print("You lost "+ str(bet))
  print("Credits: " + str(money))
  return 

#Draw a Card
cards = ["A", "A", "A", "A", "K", "K", "K", "K", "Q", "Q", "Q", "Q", "J", "J", "J", "J", "10", "10", "10", "10", "9", "9", "9", "9", "8", "8", "8", "8", "7", "7", "7", "7", "6", "6", "6", "6", "5", "5", "5", "5", "4", "4", "4", "4", "3", "3", "3", "3", "2", "2", "2", "2"]
def draw_card(bet):
  global money
  print("Draw a Card")
  playerInt = random.randint(1,52)
  playerCard = cards[playerInt]
  print("You drew a " + playerCard)
  cards.remove(playerCard)
  dealerInt = random.randint(1,51)
  dealerCard = cards[dealerInt]
  print("Dealer drew a " + dealerCard)
  if dealerInt > 15:
    dealerVal = int(dealerCard)
  elif dealerInt > 11:
    dealerVal = 11
  elif dealerInt > 7:
    dealerVal = 12
  elif dealerInt > 3:
    dealerVal = 13
  elif dealerInt < 4:
    dealerVal = 14
  if playerInt > 16:
    playerVal = int(playerCard)
  elif playerCard == "J":
        playerVal = 11
  elif playerCard == "Q":
        playerVal = 12
  elif playerCard == "K":
        playerVal = 13
  elif playerCard == "A":
        playerVal = 14
  if playerVal > dealerVal:
    print("You win " + str(bet))
    money += bet
  elif playerVal == dealerVal:
    print("Tie!")
  else:
    print("You lose " + str(bet))
    money -= bet
  print("Credits: " + str(money))
  return 
    
  
#Roulette
RouWheel = [["0", "Green", "Zero"], ["28", "Black", "Even"], ["9", "Red", "Odd"], ["26", "Black", "Even"], ["30", "Red", "Even"], ["11", "Black", "Odd"], ["7", "Red", "Odd"], ["20", "Black", "Even"], ["32", "Red", "Even"], ["17", "Black", "Odd"], ["5", "Red", "Odd"], ["22", "Black", "Even"], ["34", "Red", "Even"], ["15", "Black", "Odd"], ["3", "Red", "Odd"], ["24", "Black", "Even"], ["36", "Red", "Even"], ["13", "Black", "Odd"], ["1", "Red", "Odd"], ["00", "Green", "Zero"], ["27", "Red", "Odd"], ["10", "Black", "Even"], ["25", "Red", "Odd"], ["29", "Black", "Odd"], ["12", "Red", "Even"], ["8", "Black", "Even"], ["19", "Red", "Odd"], ["31", "Black", "Odd"], ["18", "Red", "Even"], ["6", "Black", "Even"], ["21", "Red", "Odd"], ["33", "Black", "Odd"], ["16", "Red", "Even"], ["4", "Black", "Even"], ["23", "Red", "Odd"], ["35", "Black", "Odd"], ["14", "Red", "Even"], ["2", "Black", "Even"]]
WheelHistory = []

def roulette(outside, outsideamt=20, inside=None, insideamt=0):
  global money
  if (outsideamt+insideamt) > money:
    print("You are out of Money!")
    quit
  else:
    spin = RouWheel[random.randint(0,38)]
    print("You bet " + str(outsideamt) + " on " + str(outside))
    if inside != None:
      print("You bet " + str(insideamt) + " on " + str(inside))
    print("The Wheel landed on: "+ str(spin))
    if outside == spin[1] or outside ==spin[2]:
      print("You won the outside bet!")
      money += outsideamt
    else:
      print("You lost outside bet. Try Again")
      money -= outsideamt
    if inside == spin[0]:
      print("Ball Landed on "+ spin[0] + "! Big Winner!!")
      money += insideamt * 35
    else:
      print("You lost inside bet.")
      money -= insideamt
  print("Credits: " + str(money))
  return

    

    


  
  
  

#Call your game of chance functions here
coin_toss("Heads", 20)
coin_toss("Tails", 20)
cho_han("Even", 20)
cho_han("Odd", 20)
draw_card(10)
draw_card(20)
draw_card(30)
roulette("Black", 20, "29", 5)
roulette("Black", 20, "22", 5)
roulette("Red")
roulette("Even")