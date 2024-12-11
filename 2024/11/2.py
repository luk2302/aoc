import importlib

from utils.aoc import *
from utils.simple import *

s = importlib.import_module("1").s

def solve(d: list[str]):
    stones = ints(d[0])
    return s(stones, 75)


aoc_day(__file__, solve, "input.txt", "example.txt", 65601038650482)  # EXAMPLE_MARKER
