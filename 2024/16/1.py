from utils.aoc import *

# oh my god, that code is bad
def bfs(start, target, m, valid_path, cost, full):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cheapest = {(start, (1,0)): [0, [], None, (1,0)], (start, (-1,0)): [2000, [], None, (1,0)], (start, (0,1)): [1000, [], None, (1,0)], (start, (0,-1)): [1000, [], None, (1,0)]}
    q = [(start, [start], {start}, (1,0))]
    while q:
        (e, path, path_set, looking) = q.pop(0)
        print("processing", e, looking)
        for move_dir in dirs:
            (xn, yn) = move_dir
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0]):
                if valid_path(e, n):
                    print("  stepping to", n, "in", move_dir)
                    rots_now = 0 if move_dir == looking else (2 if looking[0] == xn or looking[1] == yn else 1)
                    for new_look_dir in dirs:
                        print("    rotating to dir", new_look_dir)
                        rots_next = 2 if new_look_dir == (-move_dir[0], -move_dir[1]) else (0 if new_look_dir == move_dir else 1)

                        sum_rots = (rots_now + rots_next) % 4
                        oc = cheapest.get((n, new_look_dir))
                        nc = cheapest[(e, looking)][0] + cost(e, n) + sum_rots * 1000
                        cheaper = not oc or nc < oc[0]
                        if cheaper:
                            print("      cheaper way to", n, "facing", new_look_dir, "is", nc)
                            cheapest[(n, new_look_dir)] = [nc, None, e]

                        if n == target or m[n[1]][n[0]] == target:
                            if not full:
                                return nc
                        elif cheaper:
                            q.append((n, None, path_set.union({n}), new_look_dir))

    if full:
        return cheapest
    return None


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    for r in range(0, lc, 1):
        l = d[r]
        for x in range(w):
            if l[x] == "S":
                s = (x,r)
            if l[x] == "E":
                e = (x,r)

    c = bfs(s, "E", d, lambda f, t: d[t[1]][t[0]] != "#", lambda f,t: 1, True)

    mi = None
    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        k = (e, i)
        if k in c:
            print(c[k][0])
            if not mi:
                mi = c[k][0]
            else:
                mi = min(mi, c[k][0])

    return mi


aoc_day(__file__, solve, "input.txt", "example2.txt", 11048)  # EXAMPLE_MARKER
