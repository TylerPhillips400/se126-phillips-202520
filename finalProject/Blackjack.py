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
#deck               Populated 2D list containing all the cards from the CSV file including rank and suit
#ace_count          Counts to see if there is an ace in the hand passed to the hand_value() function
#hand               Hand or 2 cards passed to hand_value() function depending on dealer or player
#total              Counts total value of hand passed to hand_value() function depending
#card               1 card containing rank and suit which is passed to hand_value() and prioritizing rank for calculation
#player_hand        Caclulated hand value of player including suit
#dealer_hand        Caclulated hand value of dealer including suit
#show_all_dealer    If this variable is labled true then the user is able to see the dealers card after playing out their hand
#ans                If this variable = "y" the program will re run [input]
#choice             If this variable = "y" the player will "hit" if "n" then the play will stand and continue the program
#player_choice      Asks player if they would like to hit or stand [input]
#dealer_value       Calucates value of dealer hand against player hand to see who won
#player_value       Calucates value of player hand against dealer hand to see who won
#player_wins        Counting variable for player wins
#player_losses      Counting variable for player losses
#dealer_wins        Counting variable for dealer wins
#dealer_losses      Counting variable for dealer losses
#player_push        Counting variable for player ties
#dealer_push        Counting variable for dealer ties
#player_name        empty list for player names
#player_wins        empty list for player wins
#player_losses      empty list for player losses
#player_push        empty list for player ties
#player_avg         empty list for player average
#valid_menu         list for valid menu options


#-----Imports-------------------------------------------------------------------------------------
#Import os for clear() function
from os import name, system
#import the CSV (comma separated value) library and a Random library for chosen card
import csv, random
#------Functions-----------------------------------------------------------------------------------
def loopcontrol(): #() is empty so NO parameters; this function does not require any info to run
  ans = input("\nWould you like to play another hand? [y/n]: ").lower()
  #check the ans value, repeat back to user if necessary
  while ans != "y" and ans != "n":
    print("***INVALID ENTRY***")
    ans = input("Would you like to play another hand? [y/n]: ").lower()
  #return the ans value tp be used in the base program!
  return ans

def clear():
    if name == 'nt':        #windows os
        _ = system('cls')
    else:                   #linux or mac
        _ = system('clear')

def shuffle():      
    #Shuffles deck of cards for random hand for player and dealer
    random.shuffle(deck)

def deal(deck):     
    #Pulls last card and removes it from the list 'deck'
    return deck.pop()

def hand_value(hand):
    #Calculate hand values
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
    #Displays hands and if the hand is played out the dealer will show their second card
    print(f"\n    {player_name}'s hand: {player_hand}\t\tValue: {hand_value(player_hand)}")
    if show_all_dealer:
        print(f"Dealer's hand: {dealer_hand}\t\tValue: {hand_value(dealer_hand)}")
    else:
        print(f"Dealer's hand: [{dealer_hand[0]}, {['?', '?']}]")

def display(x, records):
   
    print(f"{'Player Name':15}  {'Wins':4}  {'Losses':6}  {'Ties':4}  {'Avg'}")
    print("-" * 50)
    if x != "x":
        #printing one record
        print(f"{player_name[x]:15}  {player_wins[x]:4}  {player_losses[x]:6}  {player_push[x]:4}  {player_avg[x]}%")
    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{player_name[mid]:15}  {player_wins[mid]:4}  {player_losses[mid]:6}  {player_push[mid]:4}  {player_avg[mid]}%") 
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{player_name[i]:15}  {player_wins[i]:4}  {player_losses[i]:6}  {player_push[i]:4}  {player_avg[i]}%")
    print("-" * 50)

def swap(index, listName):  #Function for bubble sorting each list
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

def menu():     #Menu function
    print("\n***Search Menu***")
    print("1. Search by NAME")
    print("2. Search by Wins")
    print("3. Search by Loses")
    print("4. EXIT")

    menu_choice = input("Enter your search type [1-4]: ")
    return menu_choice

#-----Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
deck = []
cards = []
player = []
dealer = []
found = []

#create counting variables
player_wins = 0
player_losses = 0
dealer_wins = 0
dealer_losses = 0
player_push = 0
dealer_push = 0

#-----connected to file------------------------------------------
with open("finalProject/cards.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #Changing the suits from words to symbols
        if rec[0] == "Hearts":
            rec[0] = "♥"
        elif rec[0] == "Diamonds":
            rec[0] = "♦"
        elif rec[0] == "Spades":
            rec[0] = "♠"
        elif rec[0] == "Clubs":
            rec[0] = "♣"
        
        for i in range(6):  #2D list
            deck.append(rec)
#-----disconnected from file---------------------------------------

#shuffle deck
shuffle()

#Enter player name for new record
player_name = input("Please Enter your name: ").lower()

answer = "y"

while answer == "y":
    
    player_hand = []
    dealer_hand = []

    for i in range(2):
        #Deal 2 cards to the player and dealer
        player_hand.append(deal(deck))
        dealer_hand.append(deal(deck))

    choice = "y"

    while choice == "y":
        #Hit or stand based on cards given
        display_hands(player_hand, dealer_hand)
        player_choice = input("Hit or Stand? [h/s]: ").lower()

        if player_choice == 'h':
            player_hand.append(deal(deck))
            if hand_value(player_hand) > 21:
                choice = "n"
        elif player_choice == 's':
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deal(deck))
            choice = "n"
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    #Displays the dealers hand
    display_hands(player_hand, dealer_hand, show_all_dealer=True)

    #Calculate value
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)

    #Determine winner based on value and add for precentages
    if dealer_value > 21:
        player_wins += 1
        dealer_losses += 1
        print("Dealer busts! You win!")
    elif player_value > 21:
        dealer_wins += 1
        player_losses += 1
        print("You busted! Dealer wins.")
    elif player_value > dealer_value and player_value <= 21:
        player_wins += 1
        dealer_losses += 1
        print("You win!")
    elif dealer_value > player_value and dealer_value <= 21:
        dealer_wins += 1
        player_losses += 1
        print("Dealer win!")
    elif dealer_value == player_value:
        player_push += 1
        dealer_push += 1
        print("Neither you or the dealer won. Push.")
    else:
        print()
    
    answer = loopcontrol()

#Print statements for win / loss average
total_hands = player_wins + player_losses + player_push
player_avg = (player_wins/total_hands) * 100
dealer_avg = (dealer_wins/total_hands) * 100
print(f"\nTotal Games Played: {total_hands}\n")
print(f"{player_name} had {player_wins} win(s) | {player_losses} loss(es) | {player_push} tie(s)! ")
print(f"Winning Percentage is: {player_avg:.0f}%\n ")
print(f"Dealer had {dealer_wins} win(s) | {dealer_losses} loss(es) | {dealer_push} tie(s)! ")
print(f"Winning Percentage is: {dealer_avg:.0f}%\n ")
print("Thanks for playing! And may the Odds Ever be in Your Favor!\n")

#create and write blackjackGames.csv
file = open("text_files/blackjackGames.csv", "a")
file.write(f"{player_name},{player_wins},{player_losses},{player_push},{player_avg:.0f}\n")
file.close()

#create empty list
player_name = []
player_wins = []
player_losses = []
player_push = []
player_avg = []

#we will use the below hand-populated list
valid_menu = ["1", "2", "3"]

#-----connecting to the file----------------------------------
with open("finalproject/blackjackGames.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #parallel lists --> data dispersed across lists, connected by the same index
        player_name.append(rec[0])
        player_wins.append(rec[1])
        player_losses.append(rec[2])
        player_push.append(rec[3])
        player_avg.append(rec[4])
#-----disconnected from file-----------------------

answer = "y"
while answer == "y":
    
    print("\n***Search Menu***")
    print("1. Show All Player Names")
    print("2. Search by Player Names")
    print("3. EXIT")

    search_type = input("Enter your search type [1-3]: ")
    
    #using 'not in' for user validity checks
    if search_type not in valid_menu: 
        print("!INVALID ENTRY!\nPlease try again.\n")
    elif search_type == "1": #search by NAME
        print("Show All Player Names")

        #Bubble Sort --> *Always sort Before we binary search
        for i in range(0, len(player_name) - 1):
            for j in range(0, len(player_name) - 1):
                if player_name[j] > player_name[j + 1]:
                    temp = player_name[j]
                    player_name[j] = player_name[j + 1]
                    player_name[j + 1] = temp
                    #SWAP!
                    swap(j, player_wins)
                    swap(j, player_losses)
                    swap(j, player_push)
                    swap(j, player_avg)
        
        display("x", len(player_name)) #call display() to show the values

    elif search_type == "2":
        print(f"\nYou have chosen to search by Player Name\n")

        search = input("Which Player are you looking for: ").lower()

        min = 0
        max = len(player_name) - 1
        mid = int((min + max) / 2)

        while min < max and search.lower() != player_name[mid].lower():
            if search.lower() < player_name[mid].lower():
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)

        if search.lower() == player_name[mid].lower():
            print(f"We found your search {search} in record {mid}: ")
            print(f"\n{'Player Name':15}  {'Wins':4}  {'Losses':6}  {'Ties':4}  {'Avg'}")
            print("-" * 50)
            print(f"{player_name[mid]:15}  {player_wins[mid]:4}  {player_losses[mid]:6}  {player_push[mid]:4}  {player_avg[mid]}%")
        else:
            print(f"\nSorry, we could not find your search for {search}. Please try again.")
   
    elif search_type == "3": 
            print("\n---EXIT---")                                            
            answer = "n"             #exit the loop
    else:
        print("\t!INVALID ENTRY!")
        #build a way out of the loop - answer should be able to change value!
        if search_type == "1" or search_type == "2":
            answer = loopcontrol()
print("\nThank You for Playing! Good Bye!\n")
