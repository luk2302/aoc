from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0

    cards = [1 for _ in range(lc)]
    for r in range(0, lc, 1):
        l = d[r]

        _, g = l.split(": ")
        w, p = g.split(" | ")
        w = [int(x) for x in w.split(" ") if x.strip()]
        p = [int(x) for x in p.split(" ") if x.strip()]
        m = len(set(w).intersection(set(p)))

        for c in range(m):
            if r + 1 + c < lc:
                cards[r + 1 + c] += cards[r]

    return sum(cards)


aoc_day(__file__, solve, "input.txt", "example.txt", 30)  # EXAMPLE_MARKER
