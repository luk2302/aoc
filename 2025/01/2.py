from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    c = 50
    for r in range(0, lc, 1):
        l = d[r]
        rot = l[0]
        am = int(l[1:])

        if am >= 100:
            solution += am // 100
            am = am % 100
        o = c
        c += -am if rot == "L" else am
        if o != 0 and c <= 0 or c >= 100:
            solution += 1
        c = (c + 100) % 100

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 6)  # EXAMPLE_MARKER
