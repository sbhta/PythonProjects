import random
from time import sleep
from classes import *


# creating the deck
deck = []
for num in range(2, 15):
    for suite in range(1, 5):
        deck.append(Card(num, suite))

random.shuffle(deck)

for i in deck:
    if i.suite == 1: i.suite = "♠"
    elif i.suite == 2: i.suite = "♥"
    elif i.suite == 3: i.suite = "♣"
    elif i.suite == 4: i.suite = "♦"

    if i.value == 11: i.value = "J"
    elif i.value == 12: i.value = "Q"
    elif i.value == 13: i.value = "K"
    elif i.value == 14: i.value = "A"

# giving cards to the player and dealer

player_hand = [deck.pop(), deck.pop()]
player_hand_value = 0
dealer_hand = [deck.pop(), deck.pop()]
dealer_hand_value = 0

print("THE DEALERS HAND:")
print("# {} {} {} #".format(dealer_hand[0].suite, dealer_hand[0].value, dealer_hand[0].suite), end="    ")
print("# ? ? ? #")

def add_to_value(hand_value, num):
    if num == "J": hand_value += 10
    elif num == "Q": hand_value += 10
    elif num == "K": hand_value += 10
    elif num == "A":
        if hand_value + 11 > 21: hand_value += 1
        else: hand_value += 11
    else: hand_value += num
    return hand_value



def show_player_card():
    print("""
    YOUR HAND:""")
    for i in player_hand:
        print("# {} {} {} #".format(i.suite, i.value, i.suite), end="    ")

def show_dealer_card():
    print("""
    YOUR HAND:""")
    for i in dealer_hand:
        print("# {} {} {} #".format(i.suite, i.value, i.suite), end="    ")

show_player_card()

player_hand_value = add_to_value(player_hand_value, player_hand[0].value)
player_hand_value = add_to_value(player_hand_value, player_hand[1].value)

dealer_hand_value = add_to_value(dealer_hand_value, dealer_hand[0].value)
dealer_hand_value = add_to_value(dealer_hand_value, dealer_hand[1].value)

for i in range(1, 5):
    if player_hand_value <= 21:
        inp = input("""
    More?(y/n)""")
        if inp == "y":
            player_hand.append(deck.pop())
            player_hand_value = add_to_value(player_hand_value, player_hand[-i].value)
            show_player_card()
        elif inp == "n":
            print("""
    please wait for the dealers to draw a card...""")
            sleep(1)
            if dealer_hand_value < 17:
                dealer_hand.append(deck.pop())
                dealer_hand_value = add_to_value(dealer_hand_value, dealer_hand[-1].value)


            print("""
    ## THE CURRENT TABLE ##""")

            print("""
    dealers cards: """, end="   ")
            for i in dealer_hand:
                print("# {} {} {} #".format(i.suite, i.value, i.suite), end="    ")

            print("""
    players cards: """, end="   ")
            for i in player_hand:
                print("# {} {} {} #".format(i.suite, i.value, i.suite), end="    ")

            print("""
            
    your card value {}
    dealers card value {}""".format(str(player_hand_value), str(dealer_hand_value)))
            if dealer_hand_value > player_hand_value:
                print("""
    IM VERY SORRY BUT YOU LOST (LOL)""")
            elif dealer_hand_value < player_hand_value:
                print("""
    YOU WON, NICE (shit)""")
            elif dealer_hand_value == player_hand_value:
                print("""
    OH NO, A DRAW, BETTER LUCK NEXT TIME!""")

            break



        else:
            print("""
    please enter a valid answer""")

    else:
        for card in player_hand:
            if card.value == 11:
                card.value = 1
        if player_hand_value > 22:
                 print("""
             SORRY, YOU LOST""")
                 break
