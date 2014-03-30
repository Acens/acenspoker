import collections
import intertools
import random


class poker_hand():


    def __init__(self, card_list):
        self.card_list = card_list


    def __repr__(self):
        short_desc = "Nothing."
        numeral_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.numeral] += 1
            suit_dict[my_card.suit] += 1

        # Pair
        if len(numeral_dict) == 4:
            short_desc = "One pair."

        # Two pair or 3-of-a-kind
        elif len(numeral_dict) == 3:
            if 3 in numeral_dict.values():
                short_desc ="Three-of-a-kind."
            else:
                short_desc ="Two pair."

        # Full house or 4-of-a-kind
        elif len(numeral_dict) == 2:
            if 2 in numeral_dict.values():
                short_desc ="Full house."
            else:
                short_desc ="Four-of-a-kind."
        else:

            # Flushes and straights
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_numeral = min([SUITS.index(x) for x in numeral_dict.keys()])
            max_numeral = max([RANKS.index(x) for x in numeral_dict.keys()])
            if int(max_numeral) - int(min_numeral) == 4:
                straight = True

            # Ace can be low
            low_straight = set(("Ace", "2", "3", "4", "5"))
            if not set(numeral_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                short_desc ="Straight."
            elif flush and not straight:
                short_desc ="Flush."
            elif flush and  straight:
                short_desc ="Straight flush."
        enumeration = "/".join([str(x) for x in self.card_list])
        return "{enumeration} ({short_desc})".format(**locals())
