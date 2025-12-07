from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    l = d[0].split(",")
    for x in l:
        s,e = ints(x)
        for a in range(s,e + 1):
            s = str(a)
            if s == s[:len(s) // 2] + s[:len(s) // 2]:
                solution += a


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 1227775554)  # EXAMPLE_MARKER
