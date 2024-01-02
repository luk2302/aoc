from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    m = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in d:
        for k in range(len(m)):
            i = i.replace(m[k], m[k] + str(k+1) + m[k])
        a = [c for c in i if c.isnumeric()]
        solution = solution + int(a[0] + a[-1])

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 281)
