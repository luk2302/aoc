from utils.aoc import aoc_day


def solve(d: list[str]):
    d = [x + "." for x in d]
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]
        start = -1
        end = -1
        for r2 in range(0, w, 1):
            if l[r2].isdigit():
                if start < 0:
                    start = r2
                end = r2
            else:
                if start >= 0:
                    valid = False
                    for x in [r-1, r, r+1]:
                        for y in range(start-1, end+2):
                            if 0 <= x < lc and 0 <= y < w and (not d[x][y].isdigit() and d[x][y] != "."):
                                valid = True
                    if valid:
                        solution += int(l[start:end+1])
                    start = -1

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt",4361)  # EXAMPLE_MARKER
