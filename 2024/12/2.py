from utils.aoc import *


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    consumed = set()
    for r in range(0, lc, 1):
        l = d[r]
        for x in range(w):
            if (x,r) in consumed:
                continue
            cr = l[x]
            queue = [(x,r)]
            area = set()
            visited = set()
            while len(queue) != 0:
                n = queue.pop()
                visited.add(n)
                if d[n[1]][n[0]] == cr:
                    area.add(n)
                    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        n2 = (n[0] + i[0], n[1] + i[1])
                        if n2 not in visited and 0 <= n2[0] < w and 0 <= n2[1] < lc:
                            queue.append(n2)

            fencing = set()
            for a in area:
                consumed.add(a)
                for f in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    n = (f[0] + a[0], f[1] + a[1])
                    if not (0 <= n[0] < w and 0 <= n[1] < lc) or d[n[1]][n[0]] != cr:
                        fencing.add(("|" if f[0] != 0 else "-", n, a[0] if f[0] != 0 else a[1]))

            sides = 0
            counted = set()
            for fence in fencing:
                if fence not in counted:
                    sides += 1
                    counted.add(fence)
                    i = 0
                    dirs = {(0, -1), (0, 1)} if fence[0] == "|" else {(-1, 0), (1, 0)}
                    while dirs:
                        i += 1
                        d2 = dirs.copy()
                        for f2 in dirs:
                            n2 = (f2[0] * i + fence[1][0], f2[1] * i + fence[1][1])
                            if (fence[0], n2, fence[2]) in fencing:
                                counted.add((fence[0], n2, fence[2]))
                            else:
                                d2.remove(f2)
                        dirs = d2
            solution += len(area) * sides
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 1206)  # EXAMPLE_MARKER
