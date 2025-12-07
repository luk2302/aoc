from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for y in range(0, lc, 1):
        for x in range(w):
            if d[y][x] != "@":
                continue
            sum = 0
            for (dx, dy) in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                rx = x + dx
                ry = y + dy
                if not (0 <= rx < w and 0 <= ry < lc):
                    continue
                if d[ry][rx] == "@":
                    sum += 1
            if sum < 4:
                solution += 1

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 13)  # EXAMPLE_MARKER
