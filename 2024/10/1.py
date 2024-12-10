from utils.aoc import *

def search(start, m):
    q = [(start, [start], {start})]
    valids = []
    while q:
        (e, path, path_set) = q.pop(0)
        for (xn, yn) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0]):
                if m[e[1]][e[0]] + 1 == m[n[1]][n[0]]:
                    if m[n[1]][n[0]] == 9:
                        valids.append(n)
                    elif n not in path_set:
                        q.append((n, path + [n], path_set.union({n})))
    return valids

def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    m = []
    s = []
    for r in range(0, lc, 1):
        m.append([int(x) for x in d[r]])
        for x in range(w):
            if m[r][x] == 0:
                s.append((x,r))

    for xs in s:
        solution += len(set(search(xs, m)))
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 36)  # EXAMPLE_MARKER
