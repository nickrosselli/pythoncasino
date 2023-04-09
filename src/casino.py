import helpers as h
import games as g

balance = 1000 # This will be changed later to actually store data in a db
keepGoing = True
menu = f"""
**************
Python Casino             
**************
Balance: ${balance}       
**************
1. Blackjack
2. Slots
3. Roulette
4. Quit
**************
Enter a selection: """

while keepGoing == True:
    choice = h.getInt(menu)
    if choice == 1:
        g.blackjack()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Ok goodbye.")
        keepGoing = False
    else:
        print("That is not a valid selection. Please try again")