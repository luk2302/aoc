from functools import cache
from utils.aoc import *

@cache
def possible(t:str, all_ts:tuple[str]):
    if len(t) == 0:
        return 1
    pos = sum(possible(t[len(ts):], all_ts) for ts in all_ts if t.startswith(ts))
    return pos


def solve(d: str):
    all_ts, ts = d.split("\n\n")
    solution = 0
    all_ts = (*all_ts.split(", "),)
    ts = ts.split("\n")

    for t in ts:
        solution += possible(t, all_ts)

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 16, "FULL")  # EXAMPLE_MARKER
