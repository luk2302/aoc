from utils.aoc import *


def solve(d: list[str]):
    lc = len(d)
    solution = 0
    for r in range(0, lc, 1):
        l = int(d[r])
        for i in range(2000):
            l = ((l * 64) ^ l) % 16777216
            l = ((l // 32) ^ l) % 16777216
            l = ((l * 2048) ^ l) % 16777216
        solution += l
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 37327623)  # EXAMPLE_MARKER
