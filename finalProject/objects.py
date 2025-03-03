import csv 
import random

class Card: #a class constructor for a playing card
  def __init__(self, suit, rank, char, value):
    self.suit = suit
    self.rank = rank
    self.char = char
    self.value = value

deck = [] #1D list to hold all cards - this will be populated with objects (cards)

with open("finalProject/cards.csv") as csvfile:
  file = csv.reader(csvfile)
  for rec in file:

    if rec[0] == "Hearts":
        char = "♥"
    elif rec[0] == "Diamonds":
        char = "♦"
    elif rec[0] == "Spades":
        char = "♠"
    elif rec[0] == "Clubs":
        char = "♣"


    if rec[1].isdigit():
       value =int(rec[1])
    elif rec[1] in ['K', 'J', 'Q']:
       value = 10
    else:
       value = 1

    deck.append(Card(rec[0], rec[1], char, value))

print("---ORIGINAL---------------------------------")
for i in range(len(deck)):
  print(f"CARD: {deck[i].rank} {deck[i].char} - Suit: {deck[i].suit}  Value:{deck[i].value}")

print(f"\n#13: {deck[13].rank}  {deck[13].suit}\n")


random.shuffle(deck)

print("\n---SHUFFLED---------------------------------")
for i in range(len(deck)):
  print(f"{deck[i].rank} {deck[i].suit}")

print(f"\n#13: {deck[13].rank}  {deck[13].suit}")


hand = [deck[0], deck[13], deck[15]]