import random


# The deck needs to be randomly initialized at the beggining of each game. Each player gets 26 cards.
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.names = {10: "Jack", 11: "Queen", 12: "King", 13: "Ace"}

    def __repr__(self):
        # print string repr of a card object
        if self.value in self.names:
            # If the value of the card is 10, 11, 12 or 13, it returns the name of the card instead of its value
            return f"{self.names[self.value]} of {self.suit}"
        else:
            # returns the value and suit of the card
            return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):  # initialize deck of cards
        # list of all possible cards in the deck
        self.cards = [
            Card(value, suit)
            for value in range(1, 14)
            for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]
        ]
        # shuffle the deck
        random.shuffle(self.cards)
        self.player_one = self.cards[:26]
        self.player_two = self.cards[26:]

    def __len__(self):
        return len(self.cards)


class AddCards:
    def __init__(self, new_cards):
        self.cards = []
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def remove_one(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"{len(self.cards)} cards"
