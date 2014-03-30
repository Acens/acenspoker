from random import shuffle


class Card(object):
    SUITS = 'SHDC'
    RANKS = ["A", 2, 3, 4, 5, 6,
             7, 8, 9, 10, "J", "Q", "K"]

    # A card is an Object with a suit and rank
    # attributes.
    def __init__(self, rank, suit):
        # To create a new Card, we pass in strings
        # representing the rank and suit (e.g.,
        # "A" and "H" for the ace of hearts).
        # We then populate a new Card object
        # with the appropriate information.
        self.rank = rank
        self.suit = suit
    
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value not in Card.RANKS:
            raise ValueError("Invalid Card Rank")
        self._rank = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if value not in Card.SUITS:
            raise ValueError("Invalid Card Suit")
        self._suit = value

    def __str__(self):
        # This function defines a string used to print
        # this object.
        return str(self.rank) + self.suit


class Deck(object):
    # A Deck is an Object which contains a list of Cards.
    def __init__(self):
        # Create a new deck of cards.
        self.cards = []
        for r in Card.RANKS: 
            for s in Card.SUITS:
                new_card = Card(r, s)
                self.cards.append(new_card)
        # The random module contains a number of useful
        # functions including one that randomly reorders
        # a list.
        self.shuffle_deck()

    def __str__(self):
        # This returns a string representing the Deck.  Defining
        # this function allows `print deck' to work properly.
        s = ""
        for c in self.cards:
            s = s + c.__str__() + " "
        return "[ " + s + "]"

    def shuffle_deck(self):
        # Return a random permutation of the cards in the
        # deck.
        shuffle(self.cards)

    def next_card(self):
        # Remove and return the first card from the deck.
        c = self.cards.pop(0)
        return c

    def __len__(self):
        # Ask how many cards are left in the deck.
        return len(self.cards)
