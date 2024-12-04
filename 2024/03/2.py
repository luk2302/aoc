import math
import re
from utils.aoc import *
from utils.simple import *


def solve(d: str):
    solution = 0
    enabled = True
    for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", d):
        if 'do' in match:
            enabled = 'don' not in match
        elif enabled:
            solution += math.prod(ints(match[4:-1]))

    return solution


aoc_day(__file__, solve, "input.txt", "example2.txt", 48, 'FULL')  # EXAMPLE_MARKER
