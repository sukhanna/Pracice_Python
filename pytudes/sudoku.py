#soduko solver 9X9

# -----rules------
#A puzzle is solved if the squares in each unit are filled with a permutation of the digits 1 to 9.
#That is, no digit can appear twice in a unit, and every digit must appear once.
#This implies that each square must have a different value from any of its peers.
#Here are the names of the squares, a typical puzzle, and the solution to the puzzle:

# A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5 
# B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
# C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6 
#---------+---------+---------    ------+------+------    ------+------+------
# D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9 
# E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2 
# F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8 
#---------+---------+---------    ------+------+------    ------+------+------
# G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1 
# H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4 
# I1 I2 I3| I4 I5 I6| I7 I8 I9    1 . 4 |. . . |. . .     1 6 4 |8 7 5 |2 9 3

# ----------terminologies -----------
# rows are numbered from A-I and columns are numbered from 1-9
# square - is a an intersection of row and column. i.e. A1,B1 etc.
# unit - is a 3X3 sub grid or region within a bigger grid i.e A1-A3,B1-B3,C1-C3
#        Every square has exactly 3 units.
# unit list - is a collection of columns unit, rows unit and box unit. In total
#             there are 27 units
# peer - is a list of all squares related to the 3 units of a square except square
#       itself i.e peer of C2 is A1 A2 A3
#                                B1 B2 B3
#                                C1 -- C3 C4 C5 C6 C7 C8 C9
#                                   D2
#                                   E2
#                                   F3
#                                   G2
#                                   H2
#                                   I2

def cross(A,B):
    return[a+b for a in A for b in B]

digits = "123456789"
rows = "ABCDEFGHI"
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, col) for col in cols] +
            [cross(row, cols) for row in rows] +
            [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")])
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

def test():
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print("All tests pass.")

def parse_grid(grid):
    """ Convert grid into dictionary of {square:digits} where square is 'A1', "A2'..
        and digits are '123456789' or return FALSE if contradiction is detected."""
    ## To start, every square can be a digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

# It turns out that the fundamental operation is not assigning a value, but rather eliminating
# one of the possible values for a square, which we implement with eliminate(values, s, d).
# Once we have eliminate, then assign(values, s, d) can be defined as "eliminate all the values from s except d".

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propogate.
    Return values, except return FALSE if a contrdiction is detected."""
    other_values = values[s].replace(d, "")
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propogate when values or places <= 2.
    Return vaues, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminiated
    values[s] = values[s].replace(d, '')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF':
            print(line)
    print()
