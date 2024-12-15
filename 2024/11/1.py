from collections import defaultdict

from utils.aoc import *
from utils.graph import *
from utils.simple import *


def s(stones:list[int], steps):
    c = 0
    stones_c = defaultdict(lambda: 0)
    for st in stones:
        stones_c[st] += 1

    for step in range(1, steps + 1):
        new = defaultdict(lambda: 0)
        for stone, cnt in stones_c.items():
            if stone == 0:
                new[1] += cnt
            elif ceil(log10(stone + 1)) % 2 == 0:
                ss = str(stone)
                new[int(ss[:len(ss)//2])] += cnt
                new[int(ss[len(ss)//2:])] += cnt
            else:
                new[stone * 2024] += cnt
        stones_c = new
    return sum(stones_c.values()) + c


def solve(d: list[str]):
    stones = ints(d[0])
    return s(stones, 25)


aoc_day(__file__, solve, "input.txt", "example.txt", 55312)  # EXAMPLE_MARKER
