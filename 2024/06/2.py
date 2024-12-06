from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
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
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    obs = set()
    sx = px
    sy = py
    sdir = dir
    while True:
        print((px, py), dir)
        nx = px + dir[0]
        ny = py + dir[1]
        try:
            if d[ny][nx] == "#":
                dir = dirs[(dirs.index(dir) + 1) % len(dirs)]
            else:
                if nx != sx or ny != sy:
                    try:
                        nd = sdir
                        nx2 = sx
                        ny2 = sy
                        ps2 = {sx, sy, sdir}
                        while 0 <= nx2 < w and 0 <= ny2 < lc:
                            px2 = nx2 + nd[0]
                            py2 = ny2 + nd[1]
                            if d[py2][px2] == "#" or (px2 == nx and py2 == ny):
                                nd = dirs[(dirs.index(nd) + 1) % len(dirs)]
                                ps2.add((nx2, ny2, nd))
                                continue
                            else:
                                nx2 = px2
                                ny2 = py2
                                if (nx2, ny2, nd) in ps2:
                                    if (nx, ny) not in obs:
                                        print('possible', (nx, ny))
                                        obs.add((nx, ny))
                                    break
                                else:
                                    ps2.add((nx2, ny2, nd))
                    except IndexError:
                        pass
                px = nx
                py = ny
        except IndexError:
            break

    return len(obs)


aoc_day(__file__, solve, "input.txt", "example.txt", 6)  # EXAMPLE_MARKER
