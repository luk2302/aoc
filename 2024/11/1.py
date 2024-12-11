from utils.aoc import *
from utils.graph import *
from utils.simple import *
from functools import cache

@cache
def rem(i, remaining):
    if remaining <= 1:
        return 1
    if i == 0:
        return rem(1, remaining - 1)
    if i < 5:
        if remaining == 2:
            return 2
        s = 0
        for ii in str(i * 2024):
            s += rem(int(ii), remaining - 3)
        return s
    if i >= 5:
        if remaining == 2:
            return 1
        if remaining == 3:
            return 2
        if remaining == 4:
            return 4
        s = 0
        for ii in str(i * 2024 * 2024):
            s += rem(int(ii), remaining - 5)
        if i == 8:  # because 8 * 2024 * 2024 results in a trailing 08 which is no longer split but directly turned into an 8 one step earlier
            s += rem(8, remaining - 4) - rem(8, remaining - 5) - rem(0, remaining - 5)
        return s

def s(stones:list[int], steps):
    c = 0
    for step in range(1, steps + 1):
        remaining = steps - step
        new = []
        for s in stones:
            if s < 10:
                c += rem(s, remaining + 1)
            elif ceil(log10(s + 1)) % 2 == 0:
                ss = str(s)
                if len(ss) == 2:
                    c += rem(int(ss[0]), remaining) + rem(int(ss[1]), remaining)
                else:
                    new.append(int(ss[:len(ss)//2]))
                    new.append(int(ss[len(ss)//2:]))
            else:
                new.append(s * 2024)
        stones = new
    return len(stones) + c


def solve(d: list[str]):
    stones = ints(d[0])
    return s(stones, 25)


aoc_day(__file__, solve, "input.txt", "example.txt", 55312)  # EXAMPLE_MARKER
