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

        c += am * (-1 if rot == "L" else 1)
        c = (c + 100) % 100
        if c == 0:
            solution += 1


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 3)  # EXAMPLE_MARKER
