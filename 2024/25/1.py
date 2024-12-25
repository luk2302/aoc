from utils.aoc import *


def solve(d: str):
    inps = d.split("\n\n")
    locks = []
    keys = []

    for inp in inps:
        inp = inp.split("\n")
        d = [sum(1 for y in range(5) if inp[y+1][x] == "#") for x in range(5)]
        if inp[0] == ".....":
            keys.append(d)
        else:
            locks.append(d)

    solution = 0
    for lock in locks:
        for key in keys:
            if all(lock[i] + key[i] <= 5 for i in range(5)):
                solution += 1

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 3, "FULL")  # EXAMPLE_MARKER
