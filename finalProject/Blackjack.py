#Tyler Phillips and Ken Pierson
#SE126.04
#Backjack
#2-26-2025

#PROMPT: 

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records


#-Imports-------------------------------------------------------------------------------------
#Import os for clear() function
from os import name, system
#import the CSV (comma separated value) library
import csv
#Import Random library for chosen card
import random
#-Functions-----------------------------------------------------------------------------------
def clear():
    if name == 'nt':        #windows os
        _ = system('cls')
    else:                   #linux or mac
        _ = system('clear')

def shuffle():
    random.shuffle(deck)

def display(card):
    print(f"{card[1]} of {card[0]}")

def deal(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
deck = []
turn = []
player = []
dealer = []

#Counting variable


#--connected to file------------------------------------------
with open("finalProject/cards.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        deck.append(rec)
#--disconnected from file---------------------------------------

#Deck Display
'''
print(f"{'SUIT':10} {'RANK'}")
print("---------------------------------------------")
for i in range(len(deck)):
    print(f"{deck[i][0]:10} {deck[i][1]}")
print("---------------------------------------------")
'''
shuffle()

deal(dealer)
deal(player)

print(dealer)
print(player)