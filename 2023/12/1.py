from utils.aoc import *
from utils.graph import *
from utils.simple import *

def cnt(s,m):
    if len(m) == 0:
        return 0 if '#' in s else 1
    if len(m) > 0 and len(s) < m[0]:
        return 0
    if len(s) == 0:
        if len(m) > 0:
            return 0
        return 1
    if s[0] == '.':
        return cnt(s[1:], m)

    a = 0
    p = all(x != '.' for x in s[:m[0]])
    n = len(s) == m[0] or s[m[0]] != '#'
    if s[0] == '?':
        return cnt(s[1:], m) + (cnt(s[m[0] + 1:], m[1:]) if p and n else 0)

    return cnt(s[m[0] + 1:], m[1:]) if p and n else 0

def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]
        c, n = l.split(' ')
        n = ints(n)
        x = cnt(c,n)
        solution += x


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 21)  # EXAMPLE_MARKER
