from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def h(s):
    k = 0
    for a in s:
        k += ord(a)
        k *= 17
        k = k % 256
    return k


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]
        solution = sum([h(x) for x in l.split(',')])


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 1320)  # EXAMPLE_MARKER
