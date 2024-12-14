import time
from utils.aoc import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = 11 if lc == 12 else 101
    h = 7 if lc == 12 else 103
    if lc == 12:
        return -1
    robots = []
    for r in range(0, lc, 1):
        px, py = ints(d[r].split(" ")[0])
        vx, vy = [int(x) for x in d[r].split(" ")[1][2:].split(",")]
        robots.append([px, py, vx, vy])
    s = 0
    while True:
        s += 1
        ps = set()
        for r in range(len(robots)):
            px, py, vx, vy = robots[r]
            px += vx
            py += vy
            px = ((px % w) + w) % w
            py = ((py % h) + h) % h
            robots[r][0] = px
            robots[r][1] = py
            ps.add((px, py))

        candidate = False
        for (px, py) in ps:
            if (px - 1, py + 1) in ps and (px + 1, py + 1) in ps and (px + 2, py + 2) in ps and (px - 2, py + 2) in ps and (px + 3, py + 3) in ps and (px - 3, py + 3) in ps and (px + 4, py + 4) in ps and (px - 4, py + 4) in ps:
                candidate = True
                break
        if candidate:
            print(s)
            for y in range(h):
                for x in range(w):
                    if (x,y) in ps:
                        print("X", end="")
                    else:
                        print(" ", end="")
                print("|")
            # time.sleep(1)
            # up = '\033[1A'
            # clear = '\x1b[2K'
            # for y in range(h + 1):
            #     print(up, end=clear)
            return s

aoc_day(__file__, solve, "input.txt", "example.txt", -1)  # EXAMPLE_MARKER
