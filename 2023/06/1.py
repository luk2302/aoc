import os
import sys

from utils.aoc import aoc_day


def solve(d: list[str]):
    solution = 1
    t = [int(x) for x in d[0].split(": ")[1].split(" ") if x]
    d = [int(x) for x in d[1].split(": ")[1].split(" ") if x]

    for rt, rd in zip(t, d):
        c = 0
        for ss in range(1, rt):
            dt = (rt - ss) * ss
            if dt > rd:
                c += 1
        solution *= c


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 288)  # EXAMPLE_MARKER
