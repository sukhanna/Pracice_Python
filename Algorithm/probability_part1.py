# Basic probability functions
# Examples or practice test are taken from different
# resources like Peter Norvig's notebook
# A Concrete Introduction to Probability (using Python) at Jupyter

from fractions import Fraction

# Probability of an event
def Probability(event, space):
    print event
    print space
    print (event & space)
    return Fraction(len(event & space), len(space))


# Tests
def Test():
    print Probability({2,4,6}, {1,2,3,4,5,6})

Test()
