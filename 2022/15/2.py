def solve(d):
    lc = len(d)
    ss = set()

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
        ss.add((x, y, m))

    h = 4000000
    for x in range(h):
        y = 0
        while y < h:
            for (x2, y2, m2) in ss:
                m = abs(x2 - x) + abs(y2 - y)
                if m <= m2:
                    y += m2 - m
                    break
            else:
                print(f"found {x} {y}")  # found 2895970 2601918
                return 4000000 * x + y
            y += 1


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
aoc("example.txt", 56000011)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt", 11583882601918)
print("")
print("--------------------------------------------------------------------------------------------------")
