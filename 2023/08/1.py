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

    i = 0
    cur = "AAA"
    while True:
        dii = di[i % (len(di))]
        cur = m[cur][0 if dii == "L" else 1]
        i += 1
        if cur == "ZZZ":
            return i


aoc_day(__file__, solve, "input.txt", "example.txt", 6)  # EXAMPLE_MARKER
