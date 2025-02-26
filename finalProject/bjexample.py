import random

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    ace_count = hand.count('A')
    total = 0
    for card in hand:
        if card.isdigit():
            total += int(card)
        elif card in ('J', 'Q', 'K'):
            total += 10
        elif card == 'A':
            total += 11
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_hands(player_hand, dealer_hand, show_all_dealer=False):
    print("\nYour hand:", player_hand, "Value:", calculate_hand_value(player_hand))
    if show_all_dealer:
        print("Dealer's hand:", dealer_hand, "Value:", calculate_hand_value(dealer_hand))
    else:
        print("Dealer's hand:", [dealer_hand[0], '?'])

def play_blackjack():
    deck = [str(i) for i in range(2, 11)] * 4 + ['J'] * 4 + ['Q'] * 4 + ['K'] * 4 + ['A'] * 4
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

    while True:
        display_hands(player_hand, dealer_hand)
        player_choice = input("Hit or stand? (h/s): ").lower()

        if player_choice == 'h':
            player_hand.append(deal_card(deck))
            if calculate_hand_value(player_hand) > 21:
                display_hands(player_hand, dealer_hand, show_all_dealer=True)
                print("You busted! Dealer wins.")
                return
        elif player_choice == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    display_hands(player_hand, dealer_hand, show_all_dealer=True)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer busts! You win!")
    elif player_value > dealer_value or dealer_value == player_value and player_value <= 21:
        print("You win!")
    else:
        print("Dealer wins!")

play_blackjack()