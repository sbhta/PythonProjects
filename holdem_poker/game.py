import random

class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
    def show(self):
        return """{} {}""".format(self.value, self.suite)


deck = []
for num in range(1, 14):
    for suite in range(1, 5):
        deck.append(Card(num, suite))

random.shuffle(deck)

for i in deck:
    if i.suite == 1: i.suite = "spade"
    elif i.suite == 2: i.suite = "hearts"
    elif i.suite == 3: i.suite = "clubs"
    elif i.suite == 4: i.suite = "diamonds"

    if i.value == 11: i.value = "J"
    elif i.value == 12: i.value = "Q"
    elif i.value == 13: i.value = "K"
    elif i.value == 1: i.value = "A"


