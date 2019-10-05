import random
from card import Card


values = list(Card.VALUES)
suits = list(Card.SUITS)


class Deck:
    ''' Deck of cards supporting common operations of shuffling and drawing. '''
    def __init__(self):
        self.cards = []
        self.index = 0
        for i in range(0, len(values)):
            for j in range(0, len(suits)):
                self.cards.append(Card(values[i], suits[j]))
        self.reset()
    
    def reset(self):
        random.shuffle(self.cards)
        self.index = 0

    def draw_top(self):
        card = self.cards[self.index]
        self.index = (self.index + 1) % len(self.cards)
        return card


