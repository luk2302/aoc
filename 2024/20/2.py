import importlib
from utils.aoc import *
bfs = importlib.import_module("1").bfs


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    for r in range(0, lc, 1):
        l = d[r]
        for x in range(w):
            if l[x] == "S":
                s = (x,r)

    return bfs(s, d, 20)


aoc_day(__file__, solve, "input.txt", "example.txt", -1)  # EXAMPLE_MARKER
