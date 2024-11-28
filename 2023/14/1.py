from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    d = [list(x) for x in d]
    solution = 0
    for r in range(1, lc, 1):
        l = d[r]
        print(l)
        for k in range(w):
            if l[k] == 'O':
                for u in range(r - 1, -1, -1):
                    if d[u][k] == '.':
                        d[u + 1][k] = '.'
                        d[u][k] = 'O'
                    else:
                        break

    print('...')

    for r in range(0, lc, 1):
        print(d[r])
        solution += sum(1 if x == 'O' else 0 for x in d[r]) * (lc - r)

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 136)  # EXAMPLE_MARKER
