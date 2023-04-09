# imported modules
import json
import helpers as h

f = open("./config.json")
conf = json.load(f)
f.close()

start = "\033[1m"
end = "\033[0;0m"

def blackjack():
    keepGoing = True
    balance = 1000
    if balance <= 0:
        print(conf['outOfMoney'])
    else:
        while keepGoing == True:
            bet = h.getInt("Enter your bet: ")
            if bet > balance:
                print("You can't bet more than what you have!")
            else:   
                deck = h.createDeck()
                playerHand = [deck.pop(), deck.pop()]
                dealerHand = [deck.pop(), deck.pop()]

            print(start + "\n\nDealer's Hand" + end + f": {dealerHand[0]}, ??")
            print(start + "Your hand" + end + f": {playerHand[0]}, {playerHand[1]}")

            choice = h.getString("\n\nDo you want to " + start + "hit " + end + "or " + start + "stand" + end +"? ")
            # Player's turn:
            if choice.lower() == "hit":
                print("\nYou chose to " + start + "hit" + end)
                playerHand.append(deck.pop())
                print(start + "Your hand" + end + f": {playerHand[0]}, {playerHand[1]}, {playerHand[2]}")
            elif choice.lower() == "stand":
                print("\nYou chose to " + start + "stand" + end)
            else:
                print("That is not a valid option. Please try again!")


            if h.calculateHand(playerHand) > 21:
                print("\n\nBust! " + conf['youLose'])
                balance -= bet
            elif h.calculateHand(playerHand) <= 21:
                if h.calculateHand(dealerHand) < 17:
                    dealerHand.append(deck.pop())
                    print("\nDealer chose to " + start + "hit" + end)
                    print(start + "Dealer's hand" + end + f": {dealerHand[0]}, {dealerHand[1]}, {dealerHand[2]}")
                    if h.calculateHand(dealerHand) > 21:
                        print("\n\nDealer busts. " + conf['youWin'])
                        balance += bet
                    elif h.calculateHand(dealerHand) >= h.calculateHand(playerHand):
                        print("\n\n" + conf['youLose'])
                        balance -= bet
                    else:
                        print("\n\n" + conf['youWin'])
                        balance += bet
            
            playAgain = h.getString("\n\n\nDo you want to play again? [Y/n]: ")
            if playAgain.lower() == "y":
                keepGoing = True
            elif playAgain.lower() == "n":
                print("Ok goodbye!")
                keepGoing = False


