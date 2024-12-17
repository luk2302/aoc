from utils.aoc import *

# somehow the code managed to get even worse compared to part 1, not even gonna bother to clean it up
def bfs(start, m):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cheapest = {(start, (1,0)): [0, set()], (start, (-1,0)): [2000, set()], (start, (0,1)): [1000, set()], (start, (0,-1)): [1000, set()]}
    q = [(start, (start,), {start}, (1,0))]
    while q:
        (e, path, path_set, looking) = q.pop(0)
        for move_dir in dirs:
            (xn, yn) = move_dir
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0]):
                if m[n[1]][n[0]] != "#":
                    rots_now = 0 if move_dir == looking else (2 if looking[0] == xn or looking[1] == yn else 1)
                    for new_look_dir in dirs:
                        rots_next = 2 if new_look_dir == (-move_dir[0], -move_dir[1]) else (0 if new_look_dir == move_dir else 1)

                        sum_rots = (rots_now + rots_next) % 4
                        oc = cheapest.get((n, new_look_dir))
                        nc = cheapest[(e, looking)][0] + 1 + sum_rots * 1000
                        cheaper = not oc or nc < oc[0]
                        pt = (*path, n)
                        if cheaper:
                            cheapest[(n, new_look_dir)] = [nc, {pt}]
                        elif oc and nc == oc[0]:
                            cheapest[(n, new_look_dir)][1].add(pt)

                        if m[n[1]][n[0]] == "E":
                            endpos = n
                        elif cheaper:
                            q.append((n, pt, path_set.union({n}), new_look_dir))

    cps = None
    for di in dirs:
        cost = cheapest.get((endpos, di))
        if cost:
            if not cps:
                cps = cost[0]
            else:
                cps = min(cps, cost[0])

    ps = set()
    for di in dirs:
        cost = cheapest.get((endpos, di))
        if cost and cost[0] == cps:
            paths_to_check = [*cost[1]]
            visited = set()
            while paths_to_check:
                path_to_check = paths_to_check.pop(0)
                if len(path_to_check) == 1:
                    continue
                f, t = path_to_check[-2:]
                ps.add(t)
                ps.add(f)
                move_dir = (t[0] - f[0], t[1] - f[1])
                if (f, move_dir) in visited:
                    continue
                paths_to_check += [*(cheapest.get((f, move_dir))[1])]
                visited.add((f, move_dir))

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "#":
                print(m[y][x], end="")
            elif m[y][x] in "SE":
                print(f"\x1b[6;30;42m{m[y][x]}\x1b[0m", end="")
            elif (x,y) in ps:
                print("\x1b[6;30;42mO\x1b[0m", end="")
            else:
                print(".", end="")
        print()

    return len(ps)


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    for r in range(0, lc, 1):
        l = d[r]
        for x in range(w):
            if l[x] == "S":
                s = (x,r)

    c = bfs(s, d)
    return c


aoc_day(__file__, solve, "input.txt", "example.txt", 45)  # EXAMPLE_MARKER
