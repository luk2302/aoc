from utils.aoc import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        for dy, dx in [(1,0), (1,1), (1, -1), (0, 1)]:
            for i in range(w):
                s = "".join([d[r+dy*x][i+dx*x] for x in range(4) if 0 <= r+dy*x < lc and 0 <= i+dx*x < w])
                if s in {"XMAS", "SAMX"}:
                    solution += 1
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 18)  # EXAMPLE_MARKER
