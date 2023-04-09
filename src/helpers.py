# imported modules
import json
import random

f = open("./config.json")
conf = json.load(f)
f.close()

# Functions
#--------------#
# inputted data
def getString(prompt):
    value = ""
    while value == "":
        value = input(prompt)
        if len(value) == 0:
            print(conf['emptyEntry'])
    return value

def getInt(prompt):
    valid = False
    value = ""
    while valid == False:
        try:
            value = int(getString(prompt))
            valid = True
        except ValueError:
            print(conf['invalidInt'])
    return value

def getFloat(prompt):
    valid = False
    value = ""
    while valid == False:
        try:
            value = float(getString(prompt))
            valid = True
        except ValueError:
            print(conf['invalidFloat'])
    return value

# casino functions
def createDeck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            deck.append(f"{value} of {suit}")
    random.shuffle(deck)
    return deck

def calculateHand(hand):
    total = 0
    aces = 0
    for card in hand:
        if card.split()[0].isdigit():
            total += int(card.split()[0])
        elif card.split()[0] in ['J', 'Q', 'K']:
            total += 10
        elif card.split()[0] == 'A':
            aces += 1
    for i in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total