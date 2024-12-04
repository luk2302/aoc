import math
import re
from utils.aoc import *
from utils.simple import *


def solve(d: str):
    solution = 0
    for match in re.findall(r'mul\(\d+,\d+\)', d):
        solution += math.prod(ints(match[4:-1]))

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 161, 'FULL')  # EXAMPLE_MARKER
