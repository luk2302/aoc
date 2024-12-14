from utils.aoc import *
from utils.simple import *


def solve(d: str):
    solution = 0
    machines = d.split("\n\n")

    for m in machines:
        a, b, p = map(ints, m.split("\n"))
        p = [10000000000000 + i for i in p]
        x = (p[0] * a[1] - p[1] * a[0]) / (b[0] * a[1] - b[1] * a[0])
        y = (p[0] - x * b[0]) / a[0]
        if x.is_integer() and y.is_integer():
            solution += 3 * round(y) + round(x)
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 875318608908, "FULL")  # EXAMPLE_MARKER
