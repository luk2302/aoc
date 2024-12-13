import math
from functools import cache

from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: str):
    solution = 0
    machines = d.split("\n\n")

    for m in machines:
        a, b, p = map(ints, m.split("\n"))
        p = [10000000000000 + i for i in p]
        f = a[0] / a[1]
        x = (p[0] - f * p[1]) / (b[0] - f * b[1])
        y = (p[0] - x * b[0]) / a[0]
        int_ish = lambda k: abs(round(k) - k) < 0.001
        if int_ish(x) and int_ish(y):
            solution += 3 * round(y) + round(x)
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 875318608908, "FULL")  # EXAMPLE_MARKER
