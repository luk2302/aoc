from utils.aoc import *


def solve(d: str):
    a, m = d.split("\n\n")
    s = None
    a = [list(x) for x in a.split("\n")]
    for y in range(len(a)):
        for x in range(len(a[0])):
            if a[y][x] == "@":
                s = (x,y)
                a[y][x] = "."

    p = s
    for ms in m:
        if ms == "\n":
            continue
        steps = { "<": (-1, 0), ">": (1,0), "^": (0,-1), "v": (0,1) }
        s = steps[ms]
        print("-----")
        print("stepping", ms, s)
        n = (p[0] + s[0], p[1] + s[1])
        if a[n[1]][n[0]] == "#":
            print("not possible")
            continue
        if a[n[1]][n[0]] == ".":
            p = n
            print("easily possible")
            continue

        # next is O
        n2 = n
        while True:
            n2 = (n2[0] + s[0], n2[1] + s[1])
            if a[n2[1]][n2[0]] == "#":
                print("not possible to shift")
                break
            if a[n2[1]][n2[0]] == ".":
                print("shifting")
                while n2 != n:
                    a[n2[1]][n2[0]] = "O"
                    print("shifting", n2)
                    n2 = (n2[0] - s[0], n2[1] - s[1])
                a[n[1]][n[0]] = "."
                p = n
                break

    solution = 0
    for y in range(len(a)):
        for x in range(len(a[0])):
            if a[y][x] == "O":
                solution += 100 * y + x
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 10092, "FULL")  # EXAMPLE_MARKER
