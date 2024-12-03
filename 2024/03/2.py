import re
from utils.aoc import *
from utils.simple import *


def solve(d: str):
    solution = 0
    enabled = True
    for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", d):
        if 'don' in match:
            enabled = False
            continue
        if 'do' in match:
            enabled = True
            continue
        if not enabled:
            continue
        a, b = ints(match[4:-1])
        solution += a * b

    return solution


aoc_day(__file__, solve, "input.txt", "example2.txt", 48, 'FULL')  # EXAMPLE_MARKER
