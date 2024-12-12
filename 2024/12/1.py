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
            fencing = 0
            for a in area:
                consumed.add(a)
                for f in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    n = (f[0] + a[0], f[1] + a[1])
                    if not (0 <= n[0] < w and 0 <= n[1] < lc) or d[n[1]][n[0]] != cr:
                        fencing += 1
            solution += len(area) * fencing
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 1930)  # EXAMPLE_MARKER
