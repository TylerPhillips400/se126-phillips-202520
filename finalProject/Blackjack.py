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

def deal(deck):
    return deck.pop()

def hand_value(hand):
    ace_count = hand.count('A')
    total = 0
    for card in hand:
        if card[1].isdigit():
            total += int(card[1])
        elif card[1] in ('J', 'Q', 'K'):
            total += 10
        elif card[1] == 'A':
            total += 11
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_hands(player_hand, dealer_hand, show_all_dealer=False):
    print(f"\n    Your hand: {player_hand}\t\tValue: {hand_value(player_hand)}")
    if show_all_dealer:
        print(f"Dealer's hand: {dealer_hand}\t\tValue: {hand_value(dealer_hand)}")
    else:
        print(f"Dealer's hand: [{dealer_hand[0]}, {['?', '?']}]")


#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
deck = []
cards = []
player = []
dealer = []

#--connected to file------------------------------------------
with open("finalProject/cards.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        if rec[0] == "Hearts":
            rec[0] = "♥"
        elif rec[0] == "Diamonds":
            rec[0] = "♦"
        elif rec[0] == "Spades":
            rec[0] = "♠"
        elif rec[0] == "Clubs":
            rec[0] = "♣"
        
        for i in range(6):
            deck.append(rec)
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

ans = "y"

while ans == "y":
    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deal(deck))
        dealer_hand.append(deal(deck))

    choice = "y"

    while choice == "y":
        display_hands(player_hand, dealer_hand)
        player_choice = input("Hit or Stand? [H/S]: ").lower()

        if player_choice == 'h':
            player_hand.append(deal(deck))
            if hand_value(player_hand) > 21:
                display_hands(player_hand, dealer_hand, show_all_dealer=True)
                print("You busted! Dealer wins.")
        elif player_choice == 's':
            choice = "n"
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal(deck))

    display_hands(player_hand, dealer_hand, show_all_dealer=True)

    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer busts! You win!")
    elif player_value > dealer_value or dealer_value == player_value and player_value <= 21:
        print("You win!")
    else:
            print("Dealer wins!")
    
    ans = input("Would you like to play another hand? [y/n]: ").lower
