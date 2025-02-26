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

def deal(num):
    cards_dealt = []
    for x in range(num):
        card = deck.pop()
        cards_dealt.append(card)
    return cards_dealt

def value_Convert(rank):
    value = 0
    if rank == 'Ace':
        value = 11
    elif rank == 'Jack' or rank == 'Queen' or rank == 'King':
        value = 10
    else:
        value = int(rank)
    return int(value)


def hand_value(card1, card2):
    h_value = 0
    for i in cards_dealt:
        h_value = int(card1 + card2)
    return h_value

#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
deck = []
cards = []
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

cards_dealt = deal(2)
print(cards_dealt)

print()
print(cards_dealt[0][1])
print(cards_dealt[1][1])

card1 = value_Convert(cards_dealt[0][1])
card2 = value_Convert(cards_dealt[1][1])



print(hand_value(card1, card2))
