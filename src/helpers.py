# imported modules
import json
import random
import sqlite3
from sqlite3 import Error

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
    for card in hand: 
        if isinstance(card, int):
            total += card
        elif card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            if total + 11 > 21:
                total += 1
            else: total += 11
    return total

# database 
def createConnection(dbfile):
    connection = None
    try:
        connection = sqlite3.connect(dbfile)
        print(sqlite3.version)
    except Error:
        print(Error)
    finally:
        if connection:
            connection.close()