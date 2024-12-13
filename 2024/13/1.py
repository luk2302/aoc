import math

from utils.aoc import *
from utils.simple import *
from decimal import *


def solve(d: str):
    solution = 0
    machines = d.split("\n\n")

    for m in machines:
        a, b, p = map(ints, m.split("\n"))
        f = a[0] / a[1]
        x = (p[0] - f * p[1]) / (b[0] - f * b[1])
        y = (p[0] - x * b[0]) / a[0]
        int_ish = lambda k: abs(round(k) - k) < 0.00000001
        if int_ish(x) and int_ish(y):
            solution += 3 * round(y) + round(x)
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 480, "FULL")  # EXAMPLE_MARKER
