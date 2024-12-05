from utils.aoc import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        for i in range(w):
            s = "".join([d[r+dy][i+dx] for dy, dx in [(0,0), (0, 2), (1,1), (2,0), (2, 2)] if 0 <= r+dy < lc and 0 <= i+dx < w])
            solution += bint(s in {"MSAMS", "SMASM", "MMASS", "SSAMM"})
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 9)  # EXAMPLE_MARKER
