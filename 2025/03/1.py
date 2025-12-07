from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]
        bs = [int(x) for x in l]
        d1 = max(bs[:-1])
        i = bs.index(d1)
        d2 = max(bs[i+1:])
        solution += 10 * d1 + d2


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 357)  # EXAMPLE_MARKER
