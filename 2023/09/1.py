from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0

    def s(x: list[int]):
        xs = [x]
        while True:
            n = [xs[-1][i+1] - xs[-1][i] for i in range(len(xs[-1]) - 1)]
            if all(c == 0 for c in n):
                break
            xs.append(n)

        return sum([c[-1] for c in xs])

    for r in range(0, lc, 1):
        l = d[r]
        sol = s([int(x) for x in l.split(" ")])
        solution += sol

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 114)  # EXAMPLE_MARKER
