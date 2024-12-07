from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    solution = 0

    orders = []
    o = False
    for r in range(0, lc, 1):
        l = d[r]
        if l == "":
            o = True
            continue
        if not o:
            orders.append(ints(l))
        else:
            k = ints(l)
            for (o1, o2) in orders:
                if o1 in k and o2 in k:
                    if k.index(o1) > k.index(o2):
                        break
            else:
                solution += k[len(k)//2]
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 143)  # EXAMPLE_MARKER
