from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: str):
    ranges, ingredients = d.split("\n\n")
    ranges = [ints(r) for r in ranges.split("\n")]
    ingredients = [int(i) for i in ingredients.split("\n")]
    solution = 0

    for i in ingredients:
        for r in ranges:
            if r[0] <= i <= r[1]:
                solution += 1
                break

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 3, "FULL")  # EXAMPLE_MARKER
