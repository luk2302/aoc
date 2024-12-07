from utils.aoc import *
from utils.simple import *
from operator import *

def s(i: list[int], t):
    if len(i) == 1:
        return i[0] == t
    if i[0] > t:
        return False
    for o in [add, mul]:
        if s([o(i[0], i[1])] + i[2:], t):
            return True
    return False

def solve(d: list[str]):
    lc = len(d)
    solution = 0
    for r in range(0, lc, 1):
        l = ints(d[r])
        if s(l[1:], l[0]):
            solution += l[0]
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 3749)  # EXAMPLE_MARKER
