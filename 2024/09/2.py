from utils.aoc import *


def solve(d: list[str]):
    solution = 0
    disk = []
    l = [int(x) for x in d[0]]
    free = False
    id = 0
    for i in l:
        if free:
            disk.append((i, "free"))
        else:
            disk.append((i, id))
            id += 1
        free = not free
    i = len(disk) - 1
    while i >= 0:
        if disk[i][1] == "free":
            i -= 1
            continue
        for i2 in range(i):
            if disk[i2][1] != "free":
                continue
            if disk[i2][0] == disk[i][0]:
                disk[i2], disk[i] = disk[i], disk[i2]
                break
            if disk[i2][0] > disk[i][0]:
                d = disk[i2][0] - disk[i][0]
                disk[i2] = disk[i]
                disk[i] = (disk[i][0], "free")
                disk.insert(i2 + 1, (d, "free"))
                i += 1
                break
        i -= 1

    c = 0
    for e in disk:
        if e[1] == "free":
            c += e[0]
            continue
        solution += sum((c + i) * e[1] for i in range(e[0]))
        c += e[0]
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 2858)  # EXAMPLE_MARKER
