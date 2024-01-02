from math import lcm

from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])

    di = d[0]

    m = {}
    for r in range(2, lc, 1):
        l = d[r]
        f, t = l.split(" = ")
        m[f] = t[1:-1].split(", ")

    sols = []
    curs = [k for k in m.keys() if k.endswith("A")]
    for c in curs:
        i = 0
        while True:
            dii = di[i % (len(di))]
            c = m[c][0 if dii == "L" else 1]
            i += 1
            if c.endswith("Z"):
                sols.append(i)
                break

    return lcm(*sols)


aoc_day(__file__, solve, "input.txt", "example2.txt", 6)  # EXAMPLE_MARKER
