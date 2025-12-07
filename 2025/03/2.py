from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve1(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]
        bs = [int(x) for x in l]
        while len(bs) > 12:
            pre = bs
            for candidate in range(len(bs) - 1):
                if bs[candidate] < bs[candidate + 1]:
                    bs = bs[:candidate] + bs[candidate + 1:]
                    removed = candidate
                    break
            else:
                bs = bs[:len(bs) - 1]
                removed = len(bs) - 1
            print("".join([str(pre[bi]) if bi != removed else red(pre[bi])  for bi in range(len(pre))]))
        f = "".join([str(b) for b in bs])
        print(bold(f))
        solution += int(f)

    return solution


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]
        bs = [int(x) for x in l]

        found = []
        print("inp", l)
        while len(found) < 12:
            d1 = max(bs[:len(bs) - (12 - len(found) - 1)])
            i = bs.index(d1)
            found.append(d1)
            bs = bs[i+1:]
            print("max", "".join([str(b) if len(found) < 12 else bold(green(b)) for b in found]), "rem", "".join([str(b) for b in bs]))

        solution += int("".join([str(b) for b in found]))
        print()


    return solution



aoc_day(__file__, solve, "input.txt", "example.txt", 3121910778619)  # EXAMPLE_MARKER
