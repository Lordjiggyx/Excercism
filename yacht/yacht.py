# Score categories
# Change the values as you see fit
YACHT = lambda d : 50 if len(set(d) == 1 else 0)
ONES = lambda d: sum([x for x in d if x ==1])
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    category(dice)
