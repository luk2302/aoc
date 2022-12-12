def bfs(start, target, m):
    shortest = {}
    q = [(start, [start])]
    while q:
        (e, path) = q.pop(0)
        l = len(path)
        if shortest.get(e, 9999) > l:
            shortest[e] = l
        else:
            continue
        for (xn, yn) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n = (xn + e[0], yn + e[1])
            if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0]):
                if m[n[0]][n[1]] - m[e[0]][e[1]] <= 1:
                    if n == target:
                        return len(path)
                    if n not in set(path):
                        q.append((n, path + [n]))


def solve(d):
    lc = len(d)
    w = len(d[0])
    mm = {"S": 0, "E": ord("z") - ord("a")}
    m = [[mm.get(c, ord(c) - ord("a")) for c in l] for l in d]

    start = (0, 0)
    end = (0, 0)
    for x in range(0, lc, 1):
        l = d[x]
        for y in range(0, w, 1):
            if l[y] == "S":
                start = (x, y)
            if l[y] == "E":
                end = (x, y)

    return bfs(start, end, m)



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
aoc("example.txt", 31)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
