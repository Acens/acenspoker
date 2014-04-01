'''
    Welcome to my poker game!

    To see player information write his player_tag (p1, p2, ...)

    To buy your hand write "player_tag.buy_hand()"

    To add chips write "player_tag.add_chips()"

    To bet write "player_tag.bet(list of chips)"

    To raise your bet write "player_tag.raise_(list of chips)"

    To see the deck write "deck"

    To shuffle the deck write "deck.shuffle()"

    Have fun :)
'''

import random

class Cards(object):
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{0}_{1}".format(self.value, self.suit)

    def __str__(self):
        return "Value: {0}\nSuit: {1}".format(self.value, self.suit)


class Poker_chip(object):

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        return "<{0}_{1}>".format(self.value, self.color)

    def __str__(self):
        return "Value: {0}\nColor: {1}".format(self.value, self.color)

    
class Deck(object):

    def __init__(self):
        deck = []
        for value in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
            for suit in ['Diamonds', 'Clubs', 'Hearts', 'Spades']:
                deck.append(Cards(value, suit))
        random.shuffle(deck)
        self.cards = deck
        self.size = len(deck)

    def __repr__(self):
        return "{}".format(self.cards)

    def __str__(self):
        return "Deck size: {}".format(self.size)

    def shuffle(self):
        random.shuffle(self.cards)
        
    def give_card(self):
        return self.cards.pop()

    def flop(self):
        for i in range(3):
            table.append(self.give_card())
            self.cards.pop()
        return table

    def turn(self):
        table.append(self.give_card())
        return table
    
    def river(self):
        table.append(self.give_card())
        return table
            

class Player(object):
    
    def __init__(self, name, poker_chips = []):
        self.name = name
        self.poker_chips = poker_chips
        self.hand = []
        
    def __repr__(self):
        x = 0
        for chip in self.poker_chips:
            x += chip.value 
        return "<Name: {0}, Poker chips: {1}, Hand: {2}>".format(self.name, x, self.hand)
    
    def __str__(self):
        x = 0
        for chip in self.poker_chips:
            x += chip.value 
        return "Name: {0}\nPoker chips: {1}\nHand: {2}".format(self.name, x, self.hand)


    def buy_hand(self):
        if len(self.hand) != 2:
            self.hand.append(deck.give_card())
            self.hand.append(deck.give_card())
        else:
            print "You've already got two cards."

    def add_chips(self, chip):
        if type(chip) == list:
            self.poker_chips += chip
        else:
            self.poker_chips.append(chip)


    def bet(self, chips):
        if type(chips) == list: 
            for chip in chips:
                try:
                    pot.append(chip)
                    self.poker_chips.remove(chip)
                except ValueError:
                    print "You don't have that chip!"
        else:
            try:
                pot.append(chips)
                self.poker_chips.remove(chips)
            except ValueError:
                print "You don't have that chip!"

    def raise_(self, chips):
        if type(chips) == list: 
            for chip in chips:
                try:
                    pot.append(chip)
                    self.poker_chips.remove(chip)
                except ValueError:
                    print "You don't have that chip!"
        else:
            try:
                pot.append(chips)
                self.poker_chips.remove(chips)
            except ValueError:
                print "You don't have that chip!"

    def fold(self):
        pass
    
    
class Game(object):

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        

if __name__ == '__main__':
    table = []
    pot = []
    deck = Deck()
    
    white_chip = Poker_chip(10, 'white')
    red_chip = Poker_chip(20, 'red')
    blue_chip = Poker_chip(50, 'blue')
    green_chip = Poker_chip(100, 'green')
    black_chip = Poker_chip(500, 'black')
    default_chips = [green_chip, blue_chip, blue_chip, red_chip, red_chip,
                     red_chip, red_chip, white_chip, white_chip]

    p1 = Player("Anderson", default_chips)
    p2 = Player("Computer", default_chips)

            
