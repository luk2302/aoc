def solve(d):
    lc = len(d)
    bs = set()
    yt = 2000000
    blocked = set()

    for i in range(0, lc, 1):
        l = d[i][len("Sensor at x="):]
        x, r = l.split(", y=", 1)
        x = int(x)
        y, r = r.split(": closest beacon is at x=")
        y = int(y)
        x2, y2 = r.split(", y=")
        x2 = int(x2)
        y2 = int(y2)

        m = abs(x2 - x) + abs(y2 - y)
        bs.add((x2, y2))

        o = abs(yt - y)
        if m > o:
            for off in range(-(m - o), m - o + 1):
                blocked.add(off + x)

    for (x, y) in bs:
        if y == yt:
            blocked.remove(x)

    return len(blocked)



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
aoc("example.txt", 26)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
