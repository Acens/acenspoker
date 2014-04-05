class poker_hand()


    def allmax(iterable, key=None):
        "Return a list of all items equal to the max of the iterable."
        result, maxval = [], None
        key = key or (lambda x: x)
        for x in iterable:
            xval = key(x)
            if not result or xval > maxval:
                result, maxval = [x], xval
            elif xval == maxval:
                result.append(x)
        return result


    def hand_rank(hand):
        ranks = card_ranks(hand)
        if straight(ranks) and flush(hand):
            return (8, max(ranks)) 
        elif kind(4, ranks):
            return (7, kind(4, ranks), kind(1, ranks)) # 99993 (7,9,3)
        elif kind(3, ranks) and kind(2, ranks):
            return (6, kind(3, ranks) and kind(2, ranks))
        elif flush(hand):
            return (5, ranks)
        elif straight(hand):
            return (4, ranks)
        elif kind(3, ranks):
            return (3, kind(3, ranks), ranks)
        elif two_pair(ranks):
            return (2, two_pair(ranks), ranks)
        elif kind(2, ranks):
            return (1, kind(2, ranks), ranks)
        else:
            return (0, ranks) 


    def card_ranks(hand):
        "Return a list of the ranks, sorted with higher first."
        ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
        ranks.sort(reverse=True)
        return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


    def straight(ranks):
        "Return true if the ordered ranks form a 5 card straight"
        return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5


    def flush(hand):
        "Return True if all the cards have the same suit"
        suits = [s for r,s in hand]
        return len(set(suits)) == 1


    def kind(n, ranks):
        for r in ranks:
            if ranks.count(r) == n: return r
        return None


    def two_pair(ranks):
        pair = kind(2, ranks)
        lowpair = kind(2, list(reversed(ranks)))
        if pair and lowpair != pair:
            return (pair, lowpair)
        else:
            return None


    def test():
        "Test cases for the functions in poker program"
        sf = "6C 7C 8C 9C TC".split() # Straight Flush
        fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
        fh = "TD TC TH 7C 7D".split() # Full House
        tp = "5S 5D 9H 9C 6S".split()
        fkranks = card_ranks(fk)
        tpranks = card_ranks(tp)
        assert kind(4, fkranks) == 9
        assert kind(3, fkranks) == None
        assert kind(2, fkranks) == None
        assert kind(1, fkranks) == 7
        assert two_pair(fkranks) == None
        assert two_pair(tpranks) == (9, 5)
        assert card_ranks(sf) == "TC 9C 8C 7C 6C"
        assert card_ranks(fk) == "9D 9H 9S 9C 7D"
        assert card_ranks(fh) == "TD TC TH 7C 7D"
        assert poker([sf, fk, fh]) == sf
        assert poker([fk, fh]) == fk
        assert poker([fh, fh]) == fh
        assert poker([sf]) == sf
        assert poker([sf] + 99*[fh]) == sf
        assert hand_rank(sf) == (8, 10)
        assert hand_rank(fk) == (7, 9, 7)
        assert hand_rank(fh) == (6, 10, 7)

    print test()
