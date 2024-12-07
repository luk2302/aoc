from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    a = []
    b = []
    for r in range(0, lc, 1):
        l = d[r]
        ax, bx = ints(l)
        a.append(ax)
        b.append(bx)

    solution = sum([ax * b.count(ax) for ax in a])


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 31)  # EXAMPLE_MARKER
