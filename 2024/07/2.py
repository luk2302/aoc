from utils.aoc import *
from utils.simple import *
from operator import *

def s(i: list[int], t):
    if len(i) == 1:
        return i[0] == t
    if i[0] > t:
        return False
    for o in [add, mul, concat_int]:
        if s([o(i[0], i[1])] + i[2:], t):
            return True
    return False

def concat_int(x,y):
    return int(f"{x}{y}")

def solve(d: list[str]):
    lc = len(d)
    solution = 0
    for r in range(0, lc, 1):
        l = ints(d[r])
        if s(l[1:], l[0]):
            solution += l[0]
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 11387)  # EXAMPLE_MARKER
