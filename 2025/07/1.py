from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    beams = {d[0].index("S")}
    hits = set()
    for i in range(lc):
        new_beams = set()
        for bx in beams:
            if d[i][bx] == "^":
                new_beams.add(bx - 1)
                new_beams.add(bx + 1)
                hits.add((bx,i))
            else:
                new_beams.add(bx)
        beams = new_beams

    return len(hits)


aoc_day(__file__, solve, "input.txt", "example.txt", 21)  # EXAMPLE_MARKER
