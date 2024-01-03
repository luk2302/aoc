from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    g = []

    empty_rows = set()
    for y in range(0, lc, 1):
        if all(x == "." for x in d[y]):
            empty_rows.add(y)

    empty_cols = set()
    for x in range(0, w, 1):
        if all(d[y][x] == "." for y in range(0, lc, 1)):
            empty_cols.add(x)

    for y in range(0, lc, 1):
        l = d[y]
        for x in range(0, w, 1):
            if l[x] == "#":
                g.append((x, y))

    cost = 10 if len(d) == 10 else 1000000
    for g1 in g:
        for g2 in g:
            dis = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            dis += sum([cost - 1 for x in range(min(g1[0], g2[0]), max(g1[0], g2[0])) if x in empty_cols])
            dis += sum([cost - 1 for y in range(min(g1[1], g2[1]), max(g1[1], g2[1])) if y in empty_rows])
            solution += dis

    return int(solution / 2)


aoc_day(__file__, solve, "input.txt", "example.txt", 1030)  # EXAMPLE_MARKER
