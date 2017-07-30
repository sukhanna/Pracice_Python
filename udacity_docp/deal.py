import random

# returns list of 5 hands (5 cards) for each player in numhands
def deal(numhands, n=5, deck=[x+y for x in '23456789TJQKA' for y in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i : n*(i+1)] for i in range(numhands)]


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

d = deal(1)
print d
print card_ranks(d)
