from utils.aoc import *


def solve(d: list[str]):
    lc = len(d)
    dir = None

    for r in range(0, lc, 1):
        l = d[r]
        py = r
        if ">" in l:
            px = l.index(">")
            dir = (1,0)
            break
        if "<" in l:
            px = l.index("<")
            dir = (-1,0)
            break
        if "v" in l:
            px = l.index("v")
            dir = (0, 1)
            break
        if "^" in l:
            px = l.index("^")
            dir = (0,-1)
            break
    ps = {(px, py)}
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    while True:
        nx = px + dir[0]
        ny = py + dir[1]
        try:
            if d[ny][nx] == "#":
                dir = dirs[(dirs.index(dir) + 1) % len(dirs)]
            else:
                px = nx
                py = ny
                ps.add((px, py))
        except IndexError:
            break

    return len(ps)


aoc_day(__file__, solve, "input.txt", "example.txt", 41)  # EXAMPLE_MARKER
