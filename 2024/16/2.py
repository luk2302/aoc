from collections import defaultdict

from utils.aoc import *
from utils.graph import *

# somehow the code managed to get even worse compared to part 1, not even gonna bother to clean it up
def bfs(start, m):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # cheapest = {start: {(1,0): [0, [], None], (-1,0): [2000, [], None], (0,1): [1000, [], None], (0,-1): [1000, [], None]}}
    cheapest = {(start, (1,0)): [0, set(), None, (1,0)], (start, (-1,0)): [2000, set(), None, (1,0)], (start, (0,1)): [1000, set(), None, (1,0)], (start, (0,-1)): [1000, set(), None, (1,0)]}
    q = [(start, (start,), {start}, (1,0), 0)]
    checking_paths = set()
    paths = defaultdict(lambda: [])
    step = 0
    while q:
        step += 1
        if step % 10000 == 0:
            print(step, len(q))
        (e, path, path_set, looking, old_cost) = q.pop(0)
        # if cheapest.get((e, looking))[0] < old_cost:
        #     print("skipping because cheaper")
        #     continue
        # print("processing", e, looking)
        for move_dir in dirs:
            (xn, yn) = move_dir
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0]):
                if m[n[1]][n[0]] != "#":
                    # print("  stepping to", n, "in", move_dir)
                    rots_now = 0 if move_dir == looking else (2 if looking[0] == xn or looking[1] == yn else 1)
                    # rots_pre = 0 if move_dir == old_move_dir or not old_move_dir else (2 if old_move_dir[0] == xn or old_move_dir[1] == yn else 1)
                    for new_look_dir in dirs:
                        nnnl = (new_look_dir[0] + n[0], new_look_dir[1] + n[1])
                        if m[nnnl[1]][nnnl[0]] == "#":
                            continue
                        # print("    rotating to dir", new_look_dir)
                        rots_next = 2 if new_look_dir == (-move_dir[0], -move_dir[1]) else (0 if new_look_dir == move_dir else 1)

                        sum_rots = (rots_now + rots_next) % 4
                        oc = cheapest.get((n, new_look_dir))
                        nc = cheapest[(e, looking)][0] + 1 + sum_rots * 1000
                        cheaper = not oc or nc < oc[0]
                        pt = (*path, n)
                        if cheaper:
                            # print("      cheaper way to", n, "facing", new_look_dir, "is", nc)
                            cheapest[(n, new_look_dir)] = [nc, {pt}, e]
                        elif oc and nc == oc[0]:# and pt not in oc[1]:
                            cheapest[(n, new_look_dir)][1].add(pt)
                            # cheaper = True

                        # if oc and nc == oc[0]:
                        #     print("sub path found")
                        #     print(path + [n])

                        if m[n[1]][n[0]] == "E":
                            # paths[nc].append(path)
                            endpos = n
                            print("path found", nc, len(path), len(paths[nc]))
                        elif cheaper:
                            # if (pt, new_look_dir) not in checking_paths:
                            q.append((n, pt, path_set.union({n}), new_look_dir, nc))
                            # checking_paths.add((pt, new_look_dir))

    cps = None
    for di in dirs:
        cost = cheapest.get((endpos, di))
        if cost:
            if not cps:
                cps = cost[0]
            else:
                cost = min(cps, cost[0])

    print("computing seats")
    ps = set()
    for di in dirs:
        cost = cheapest.get((endpos, di))
        if cost and cost[0] == cps:
            paths_to_check = [*cost[1]]
            visited = set()
            while paths_to_check:
                path_to_check = paths_to_check.pop(0)
                # if path_to_check in visited:
                #     continue
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

    # mini = min(paths.keys())
    # ps = set()
    # for p in paths[mini]:
    #     # print(p)
    #     for pp in p:
    #         ps.add(pp)
    print(len(ps))
    return len(ps)


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

    c = bfs(s, d)
    return c


aoc_day(__file__, solve, "input.txt", "example.txt", 45)  # EXAMPLE_MARKER
