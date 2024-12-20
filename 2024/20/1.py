import math
from collections import defaultdict
from utils.aoc import *


def bfs(start, m, max_skips):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    cheapest = {start: [0, None]}
    q = [(start, (start,), {start})]
    while q:
        (e, path, path_set) = q.pop(0)
        for move_dir in dirs:
            (xn, yn) = move_dir
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0]):
                if m[n[1]][n[0]] != "#":
                    oc = cheapest.get(n)
                    nc = cheapest[e][0] + 1
                    cheaper = not oc or nc < oc[0]
                    pt = (*path, n)
                    if cheaper:
                        cheapest[n] = [nc, pt]

                    if m[n[1]][n[0]] == "E":
                        endpos = n
                    elif cheaper:
                        q.append((n, pt, path_set.union({n})))

    cpp = cheapest.get(endpos)[1]
    skip_routes = defaultdict(lambda: math.inf)
    rev = cpp[::-1]
    for pi in range(len(rev)):
        p = rev[pi]
        (px, py) = p
        for dx in range(-max_skips, max_skips + 1):
            for dy in range(-max_skips + abs(dx), max_skips - abs(dx) + 1):
                n = (px + dx, py + dy)
                skips = abs(dx) + abs(dy)
                if not(0 <= n[0] < len(m) and 0 <= n[1] < len(m[0])):
                    continue
                if m[n[1]][n[0]] == "#":
                    continue
                cc = cheapest.get(p)[0]
                oc = cheapest.get(n)[0]
                nc = oc + skips
                cost_saving = cc - nc
                if cost_saving > 0:
                    skip_key = (p, n)
                    skip_routes[skip_key] = min(skip_routes[skip_key], cost_saving)

    skip_l2 = defaultdict(lambda: 0)
    for sr, src in skip_routes.items():
        skip_l2[src] += 1

    slc = 0
    for (sl, c) in skip_l2.items():
        if sl >= 100:
            slc += c

    return -1 if slc == 0 else slc


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    for r in range(0, lc, 1):
        l = d[r]
        for x in range(w):
            if l[x] == "S":
                s = (x,r)

    return bfs(s, d, 2)


aoc_day(__file__, solve, "input.txt", "example.txt", -1)  # EXAMPLE_MARKER
