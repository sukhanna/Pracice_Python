# -----------
# User Instructions
# 
# Write a function, allmax(iterable, key=None), that returns
# a list of all items equal to the max of the iterable, 
# according to the function specified by key. 
import random
import itertools

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    result, maxValue = [], None
    "lam = key or (lamda x : x)"
    for hand in iterable:
        xValue = key(hand)
        if not result or xValue > maxValue:
            result, maxValue = [hand], xValue
        elif xValue == maxValue:
            result.append(hand)
    return result

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        "four of a kind"
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        "full house"
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        "all of same suite"
        return (5, ranks)
    elif straight(ranks):
        "all cards are in sequence"
        return (4, max(ranks))
    elif kind(3, ranks):
        "three of a kind"
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        "pair"
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        "two of a kind"
        return (1, kind(2, ranks), ranks)
    else:
        "high card"
        return (0, ranks)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

# returns list of 5 hands (5 cards) for each player in numhands
def deal(numhands, n=5, deck=[x+y for x in '23456789TJQKA' for y in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i : n*(i+1)] for i in range(numhands)]

# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).
def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    hands = list(itertools.combinations(hand, 5))
    #ranks = [hand_rank(h) for h in hands]
    for h in hands:
        print h
        print hand_rank(h)
    
def test():
    "Test cases for the functions in poker program."
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    print deal(4)
    return 'tests pass'

best_hand("6C 7C 8C 9C TC TC TC".split())
