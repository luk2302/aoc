from math import log10, ceil


def bfs(start, target, m, valid_path, cost, full):
    cheapest = {start: [0, [], None]}
    q = [(start, [start], {start})]
    while q:
        (e, path, path_set) = q.pop(0)
        for (xn, yn) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0]):
                if valid_path(e, n):
                    oc = cheapest.get(n)
                    nc = cheapest[e][0] + cost(e, n)
                    cheaper = not oc or nc < oc[0]
                    if cheaper:
                        cheapest[n] = [nc, path + [n], e]

                    if n == target:
                        if not full:
                            return nc
                    elif n not in path_set and cheaper:
                        q.append((n, path + [n], path_set.union({n})))

    if full:
        return cheapest
    return None


# display original value, not cost
def display(res, w, h, highlight_path_to, m=None):
    bt = [highlight_path_to]
    c = highlight_path_to
    while c:
        c = res[c][2]
        bt.append(c)

    highlight = list(reversed(bt))
    length = len(highlight)
    max_res = max(m[x][y] if m else res[(x, y)][0] for x in range(h) for y in range(w) if (x, y) in res)
    ds = ceil(log10(max_res))
    for x in range(h):
        for y in range(w):
            if (x, y) in res:
                try:
                    idx = highlight.index((x, y))
                    c = idx * 8 // length + 30
                    if m:
                        print(f"\033[{c}m" + str(m[x][y]).rjust(ds) + "\033[0m", end=" ")
                    else:
                        print(f"\033[{c}m" + str(res[(x, y)][0]).rjust(ds) + "\033[0m", end=" ")
                except ValueError:
                    if m:
                        print(str(m[x][y]).rjust(ds), end=" ")
                    else:
                        print(str(res[(x, y)][0]).rjust(ds), end=" ")
            else:
                print(" " * ds, end=" ")
        print("")
