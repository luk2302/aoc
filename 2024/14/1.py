import operator
from collections import defaultdict
from functools import reduce
from utils.aoc import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = 11 if lc == 12 else 101
    h = 7 if lc == 12 else 103
    steps = 100
    qs = defaultdict(lambda: 0)
    for r in range(0, lc, 1):
        px, py = ints(d[r].split(" ")[0])
        vx, vy = [int(x) for x in d[r].split(" ")[1][2:].split(",")]
        px += steps * vx
        py += steps * vy
        px = ((px % w) + w) % w
        py = ((py % h) + h) % h
        qx = sign(px - w // 2)
        qy = sign(py - h // 2)
        if qx != 0 and qy != 0:
            qs[(qx, qy)] += 1

    return reduce(operator.mul, [y for x, y in qs.items()], 1)


aoc_day(__file__, solve, "input.txt", "example.txt", 12)  # EXAMPLE_MARKER
