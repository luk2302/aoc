from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    l = d[0].split(",")
    for x in l:
        s,e = ints(x)
        print(x)
        for a in range(s,e + 1):
            s = str(a)
            for x in range(1, len(s) // 2 + 1):

                sub = s[:x]
                constructed = sub
                while len(constructed) < len(s):
                    constructed += sub
                if s == constructed:
                    solution += a
                    break


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 4174379265)  # EXAMPLE_MARKER
