from utils.aoc import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])

    for r in range(0, lc, 1):
        l = d[r]
        sy = r
        if ">" in l:
            sx = l.index(">")
            sdir = (1,0)
            break
        if "<" in l:
            sx = l.index("<")
            sdir = (-1,0)
            break
        if "v" in l:
            sx = l.index("v")
            sdir = (0, 1)
            break
        if "^" in l:
            sx = l.index("^")
            sdir = (0,-1)
            break
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    obs = set()
    px, py = sx, sy
    dir = sdir
    while True:
        nx = px + dir[0]
        ny = py + dir[1]
        try:
            if d[ny][nx] == "#":
                dir = dirs[(dirs.index(dir) + 1) % len(dirs)]
            else:
                if nx != sx or ny != sy:
                    try:
                        dir2 = sdir
                        px2 = sx
                        py2 = sy
                        ps = {sx, sy, sdir}
                        while 0 <= px2 < w and 0 <= py2 < lc:
                            nx2 = px2 + dir2[0]
                            ny2 = py2 + dir2[1]
                            if d[ny2][nx2] == "#" or (nx2 == nx and ny2 == ny):
                                dir2 = dirs[(dirs.index(dir2) + 1) % len(dirs)]
                                ps.add((px2, py2, dir2))
                                continue
                            else:
                                px2 = nx2
                                py2 = ny2
                                if (px2, py2, dir2) in ps:
                                    obs.add((nx, ny))
                                    break
                                else:
                                    ps.add((px2, py2, dir2))
                    except IndexError:
                        pass
                px = nx
                py = ny
        except IndexError:
            break

    return len(obs)


aoc_day(__file__, solve, "input.txt", "example.txt", 6)  # EXAMPLE_MARKER
