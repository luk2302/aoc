from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def roll(d):
    lc = len(d)
    w = len(d[0])
    for r in range(1, lc, 1):
        l = d[r]
        for k in range(w):
            if l[k] == 'O':
                for u in range(r - 1, -1, -1):
                    if d[u][k] == '.':
                        d[u + 1][k] = '.'
                        d[u][k] = 'O'
                    else:
                        break


def solve(d: list[str]):
    lc = len(d)
    d = [list(x) for x in d]

    patterns = {}

    t = 1000000000
    for i in range(t):
        solution = 0
        f = ''.join([''.join(x) for x in d])
        if f in patterns:
            x = patterns[f]
            cycle = i - x
            print('cycle', cycle)
            n = i + ((t - i) // cycle) * cycle
            print('skipping to', n)
            for x in range(n, t):
                roll(d)
                d = rotate(d)
                roll(d)
                d = rotate(d)
                roll(d)
                d = rotate(d)
                roll(d)
                d = rotate(d)

            for r in range(0, lc, 1):
                solution += sum(1 if x == 'O' else 0 for x in d[r]) * (lc - r)
            return solution

        roll(d)
        d = rotate(d)
        roll(d)
        d = rotate(d)
        roll(d)
        d = rotate(d)
        roll(d)
        d = rotate(d)

        patterns[f] = i

        for r in range(0, lc, 1):
            solution += sum(1 if x == 'O' else 0 for x in d[r]) * (lc - r)
        print(i, solution)

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 64)  # EXAMPLE_MARKER
