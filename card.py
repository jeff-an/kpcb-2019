class Card:
    SUIT_ASCII = {
        "SPADE": "♠",
        "DIAMOND": "♦",
        "HEART": "♥",
        "CLUB": "♣"
    }
    SUITS = { "SPADE", "DIAMOND", "HEART", "CLUB" }
    VALUES = { "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2 }
    CARD_HEIGHT = 7

    def __init__(self, symbol, suit, hidden=False):
        if symbol not in Card.VALUES:
            raise ValueError("Invalid value {} passed to Card constructor".format(symbol))
        if suit not in Card.SUITS:
            raise ValueError("Invalid suit {} passed to Card constructor".format(suit))
        self.symbol = symbol
        self.suit = suit
        self.hidden = hidden
    
    def __repr__(self):
        ''' Allows Cards to be printed prettily with the suit and rank. '''
        lines = []
        lines.append("┌───────┐")
        if self.hidden:
            for _ in range(0, Card.CARD_HEIGHT - 2):
                lines.append("│░░░░░░░│")
        else:
            middle_width = 4 if self.symbol == 10 else 5
            lines.append("│{}{}".format(Card.SUIT_ASCII[self.suit], self.symbol) + " " * middle_width + "│")
            lines.append("│       │")
            lines.append("│   {}   │".format(Card.SUIT_ASCII[self.suit]))
            lines.append("│       │")
            lines.append("│" + " " * middle_width + "{}{}│".format(Card.SUIT_ASCII[self.suit], self.symbol))
        lines.append("└───────┘")
        return "\n".join(lines)

    def toggle_hidden(self):
        self.hidden = not self.hidden
