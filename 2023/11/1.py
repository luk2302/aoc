from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    g = []

    dn = []
    for l in d:
        dn.append(l)
        if all(x == "." for x in l):
            dn.append(l)
    d = dn
    lc = len(d)

    rx = 0
    for _ in range(0, w, 1):
        if all(d[y][rx] == "." for y in range(0, lc, 1)):
            for y in range(0, lc, 1):
                rr = list(d[y])
                rr.insert(rx, ".")
                d[y] = "".join(rr)
            rx += 1
        rx += 1
    w = len(d[0])


    for y in range(0, lc, 1):
        l = d[y]
        for x in range(0, w, 1):
            if l[x] == "#":
                g.append((x, y))

    for g1 in g:
        for g2 in g:
            dis = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            solution += dis

    return int(solution / 2)


aoc_day(__file__, solve, "input.txt", "example.txt", 374)  # EXAMPLE_MARKER
