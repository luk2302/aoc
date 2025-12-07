from collections import defaultdict
from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    beams = {d[0].index("S"): 1}
    for i in range(lc):
        new_beams = defaultdict(lambda: 0)
        for (bx, cnt) in beams.items():
            if d[i][bx] == "^":
                new_beams[bx - 1] += cnt
                new_beams[bx + 1] += cnt
            else:
                new_beams[bx] += cnt
        beams = new_beams

    return sum(beams.values())


aoc_day(__file__, solve, "input.txt", "example.txt", 40)  # EXAMPLE_MARKER
