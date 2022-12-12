from utils.graph import bfs


def solve(d):
    lc = len(d)
    w = len(d[0])
    mm = {"S": 0, "E": ord("z") - ord("a")}
    m = [[mm.get(c, ord(c) - ord("a")) for c in l] for l in d]

    end = (0, 0)
    for x in range(0, lc, 1):
        l = d[x]
        for y in range(0, w, 1):
            if l[y] == "E":
                end = (x, y)

    vp = lambda c, n: m[n[0]][n[1]] - m[c[0]][c[1]] <= 1
    cost = lambda c, n: 1
    return min(bfs((x, y), end, m, vp, cost, False) or 999 for x in range(lc) for y in range(w) if d[x][y] == "a")



def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    if not day_input or not day_input[0]:
        print("WARNING: input file empty")
        return

    solution = solve(day_input)

    print(f"solution: {solution}")
    if expected_solution:
        if expected_solution != solution:
            print(f"WARNING: solution does not match expected solution of {expected_solution}")
        else:
            print("matches expected solution :)")


aoc_day = __file__.split("/")[-2]
print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
print("")
aoc("example.txt", 29)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
