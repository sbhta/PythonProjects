import random
from classes import *


# creating the deck
deck = []
for num in range(1, 14):
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
    elif i.value == 1: i.value = "A"

# giving cards to the player and dealer

player_hand = []
player_hand = []