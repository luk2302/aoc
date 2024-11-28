from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def transpose(x):
    return list(map(list, zip(*x)))


def v(r):
    print(len(r))
    for v in range(1, len(r)):
        x = r[:v]
        y = r[v:]
        x.reverse()
        if len(x) > len(y):
            (x,y) = (y,x)

        d = sum([0 if x==y else 1 for x,y in zip(''.join([''.join(k) for k in x]), ''.join([''.join(k) for k in y[:len(x)]]))])
        if d == 1:
            return v
    return None


def s(f: str):
    r = f.split('\n')
    x = v(r)
    if x is not None:
        return 0, x
    return v(transpose(r)), 0


def solve(d: str):
    x = d.split('\n\n')
    v = 0
    h = 0
    for xs in x:
        vx, hx = s(xs)
        print(vx, hx, '')
        v += vx
        h += hx

    return v + 100 * h


aoc_day(__file__, solve, "input.txt", "example.txt", 400, 'FULL')  # EXAMPLE_MARKER
