from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: str):
    ranges, _ = d.split("\n\n")
    ranges = [ints(r) for r in ranges.split("\n")]

    while True:
        merged = False
        for i1 in range(len(ranges)):
            for i2 in range(len(ranges)):
                if i1 == i2:
                    continue
                r1 = ranges[i1]
                r2 = ranges[i2]

                if r1[0] > r2[1] or r2[0] > r1[1]:
                    continue # no overlap
                ranges[i1] = [min(r1[0], r2[0]), max(r1[1], r2[1])]
                ranges[i2] = None
                merged = True
            if merged:
                break
        if not merged:
            break
        ranges = [r for r in ranges if r]

    return sum([r[1] - r[0] + 1 for r in ranges])


aoc_day(__file__, solve, "input.txt", "example.txt", 14, "FULL")  # EXAMPLE_MARKER
