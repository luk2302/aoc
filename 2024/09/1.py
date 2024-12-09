from utils.aoc import *


def solve(d: list[str]):
    solution = 0
    disk = []
    l = [int(x) for x in d[0]]
    free = False
    id = 0
    for i in l:
        if free:
            disk += [-1] * i
        else:
            disk += [id] * i
            id += 1
        free = not free
    start = 0
    end = len(disk) - 1
    while start < end:
        if disk[start] != -1:
            start += 1
            continue
        if disk[end] == -1:
            end -= 1
            continue
        disk[start], disk[end] = disk[end], disk[start]
        start += 1
        end -= 1

    for i, e in enumerate(disk):
        if e == -1:
            break
        solution += i * e
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 1928)  # EXAMPLE_MARKER
