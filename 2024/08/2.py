from collections import defaultdict
from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    pos = defaultdict(lambda: [])
    for r in range(0, lc, 1):
        l = d[r]
        for x in range(w):
            if l[x] != ".":
                pos[l[x]].append((x,r))

    anti = set()
    for _, i in pos.items():
        for i1 in i:
            for i2 in i:
                if i1 == i2:
                    continue
                dx = i2[0] - i1[0]
                dy = i2[1] - i1[1]

                for k in range(ceil(min(abs(lc / dy), abs(w / dx)))):
                    if 0 <= i2[0] + dx * k < w and 0 <= i2[1] + dy * k < lc:
                        anti.add((i2[0] + dx * k, i2[1] + dy * k))
                    if 0 <= i1[0] - dx * k < w and 0 <= i1[1] - dy * k < lc:
                        anti.add((i1[0] - dx * k, i1[1] - dy * k))
    return len(anti)


aoc_day(__file__, solve, "input.txt", "example.txt", 34)  # EXAMPLE_MARKER
