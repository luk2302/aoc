from collections import Counter
from functools import cmp_to_key

from utils.aoc import aoc_day


cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])

    def t(x):
        cs = Counter(x)
        if len(cs) == 1:
            return 7
        if len(cs) == 2:
            if cs.most_common(1)[0][1] == 4:
                return 6
            return 5
        if len(cs) == 3:
            if cs.most_common(1)[0][1] == 3:
                return 4
            return 3
        if len(cs) == 4:
            return 2
        if len(cs) == 5:
            return 1

    hands = []
    for r in range(0, lc, 1):
        l = d[r]
        c, s = l.split(" ")
        hands.append((c, int(s), t(c)))

    def comp(i1, i2):
        t1 = i1[2]
        t2 = i2[2]
        if t1 != t2:
            return t1 - t2
        for c1, c2 in zip(i1[0], i2[0]):
            in1 = cards.index(c1)
            in2 = cards.index(c2)
            if in1 != in2:
                return in2 - in1

    hands.sort(key=cmp_to_key(comp))

    return sum([(ind + 1) * val[1] for ind, val in enumerate(hands)])


aoc_day(__file__, solve, "input.txt", "example.txt", 6440)  # EXAMPLE_MARKER
