from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)

    p = {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, 1), (-1, 0)],
        "F": [(0, 1), (1, 0)],
        "S": [(0, 1), (0, -1), (1, 0), (-1, 0)],
        ".": [],
    }

    for r in range(0, lc, 1):
        l = d[r]
        if "S" in l:
            x = l.index("S")
            ss = (x, r)
            s = [(x + xs, r + ys) for (xs, ys) in p["S"] if (-xs, -ys) in p[d[r + ys][x + xs]]]
            break

    for si in s:
        path = [ss, si]
        visited = set(path)
        while True:
            c = path[-1]
            cont = False
            for ox, oy in p[d[c[1]][c[0]]]:
                n = (c[0] + ox, c[1] + oy)
                if path[-2] == n:  # don't step back
                    continue
                if (-ox, -oy) in p[d[c[1] + oy][c[0] + ox]]:  # can we step back?
                    path.append(n)
                    visited.add(n)
                    cont = True
                    break

            if len(path) != len(visited):
                return (len(path) - 1) // 2

            if not cont:
                break


aoc_day(__file__, solve, "input.txt", "example.txt", 8)  # EXAMPLE_MARKER
