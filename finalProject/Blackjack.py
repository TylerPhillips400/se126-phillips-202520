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
        card = suit_symbols[card[0]] + card[1]
        cards_dealt.append(card)
    return cards_dealt

def value_Convert(rank):
    value = 0
    if rank == 'A':
        value = 11
    elif rank == 'J' or rank == 'Q' or rank == 'K' or rank == '10':
        value = 10
    else:
        value = int(rank)
    return int(value)

'''
def hand_value(card1, card2):
    h_value = 0
    for i in cards_dealt:
        h_value = int(card1 + card2)
    return h_value
'''
#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
deck = []
ranks = []
suits = []
cards = []
player = []
dealer = []

#Dictionary
suit_symbols = {"Hearts": "♥", 
                "Diamonds": "♦", 
                "Spades": "♠", 
                "Clubs": "♣"}

#Counting variable


#--connected to file------------------------------------------
with open("finalProject/cards.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        deck.append(rec)
        suits.append(rec[0])
        ranks.append(rec[1])
#--disconnected from file---------------------------------------


#shuffle()
ans = "y"
'''
ans = input("\nWould you like to play Blackjack? [y/n]: ").lower()

view = input("Would you like to see all cards in the deck? [y/n]: ").lower()
if view == "y":
    print(f"{'\nSUIT'} {'RANK'}")
    print("---------------------------------------------")
    for j in range(len(suits)):
        print(f"{suit_symbols[suits[j]]:4} {ranks[j]}")
    print("---------------------------------------------")
    input("\nPress ENTER to shuffle the deck...")
    '''
shuffle()

while ans == "y":
    deal_dealer = []
    deal_player = []
    deal_dealer = deal(2)
    dealer.append(deal_dealer)
    deal_player = deal(2)
    player.append(deal_player)

    print(dealer)
    print(player)
    ans = "x"





print()

card1 = value_Convert(player[0][0])
card2 = value_Convert(player[1][0])
card3 = value_Convert(dealer[0][0])
card4 = value_Convert(dealer[1][0])


'''
print(hand_value(card1, card2))

print(hand_value(card3, card4))
'''