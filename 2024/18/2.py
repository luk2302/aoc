from utils.aoc import *
from utils.simple import *


def bfs(start, target, w, h, walls):
    print(start, target, w, h, len(walls))
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cheapest = {start: [0, [], None]}
    q = [(start, [start], {start})]
    while q:
        (e, path, path_set) = q.pop(0)
        for (xn, yn) in dirs:
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < w and 0 <= n[1] < h:
                if n not in walls:
                    oc = cheapest.get(n)
                    nc = cheapest[e][0] + 1
                    cheaper = not oc or nc < oc[0]
                    if cheaper:
                        cheapest[n] = [nc, path + [n], e]

                    if n == target:
                        return nc
                    elif n not in path_set and cheaper:
                        q.append((n, path + [n], path_set.union({n})))
    return None


def solve(d: list[str]):
    w, h = (7, 7) if d[0] == "5,4" else (71, 71)
    walls = set()
    for r in range(len(d)):
        l = ints(d[r])
        walls.add((l[0], l[1]))
        if not bfs((0,0), (w-1,h-1), w, h, walls):
            return d[r]


aoc_day(__file__, solve, "input.txt", "example.txt", "6,1")  # EXAMPLE_MARKER
