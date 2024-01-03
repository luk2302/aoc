from utils.aoc import aoc_day

p = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],  # up right
    "J": [(0, -1), (-1, 0)],  # up left
    "7": [(0, 1), (-1, 0)],  # down left
    "F": [(0, 1), (1, 0)],  # down right
    "S": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    ".": [],
}


def solve(d: list[str]):
    lc = len(d)

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
                return cnt(d, path)

            if not cont:
                break


def cnt(d, path):
    sdiffs = [(path[1][0] - path[0][0], path[1][1] - path[0][1]), (path[-2][0] - path[0][0], path[-2][1] - path[0][1])]
    for k in ["|", "-", "L", "J", "7", "F"]:
        if all(t in sdiffs for t in p[k]):
            stype = k

    path = set(path)
    filled = set()

    for y in range(len(d)):
        inside = False
        lastseg = None
        for x in range(len(d[0])):
            if (x, y) in path:
                seg = d[y][x]
                if seg == "S":
                    seg = stype
                if seg == "|":
                    inside = not inside
                if (seg == "7" and lastseg == "L") or (seg == "J" and lastseg == "F"):
                    inside = not inside
                if seg in ["J", "L", "7", "F"]:
                    lastseg = seg

            elif inside:
                filled.add((x, y))

            # the following is basically a flood fill and works but turns out to be entirely unnecessary... :facepalm:
            # if not (x, y) in path and inside and (x, y) not in filled:
            #     fills = set()
            #     fills.add((x, y))
            #     print("\nfilling", fills, len(filled))
            #     while fills:
            #         print(fills)
            #         fill = fills.pop()
            #         if fill in filled or fill in path:
            #             continue
            #         if fill not in path:
            #             filled.add(fill)
            #             nfills = [(fill[0] + xo, fill[1] + yo) for xo, yo in [(1, 0), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1), (0, -1), (0, 1)]]
            #             nfills = {x for x in nfills if x not in filled and x not in path}
            #             fills = fills.union(nfills)
            #     print("done", len(filled))

    return len(filled)


aoc_day(__file__, solve, "input.txt", "example3.txt", 8)  # EXAMPLE_MARKER
