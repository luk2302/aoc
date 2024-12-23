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
        i = ints(l)
        for i2 in range(len(i)):
            k = i[:i2] + i[i2+1:]
            k = list(zip(k[:-1], k[1:]))
            x = [a - b for a, b in k]
            if all(1 <= abs(z) <= 3 for z in x):
                if len({1 if z > 0 else -1 for z in x}) == 1:
                    solution += 1
                    break


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 4)  # EXAMPLE_MARKER
