from functools import cache
from utils.aoc import *
from utils.simple import *

@cache
def possible(t:str, all_ts:tuple[str]):
    if len(t) == 0:
        return True
    return any(possible(t[len(ts):], all_ts) for ts in all_ts if t.startswith(ts))


def solve(d: str):
    all_ts, ts = d.split("\n\n")
    all_ts = (*all_ts.split(", "),)
    ts = ts.split("\n")

    solution = 0
    for t in ts:
        solution += bint(possible(t, all_ts))
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 6, "FULL")  # EXAMPLE_MARKER
