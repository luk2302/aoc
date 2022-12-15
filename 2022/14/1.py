def solve(d):
    lc = len(d)
    data = {}
    for i in range(0, lc, 1):
        l = d[i]
        ls = l.split(" -> ")
        last = None
        for l1 in ls:
            x, y = l1.split(",")
            x = int(x)
            y = int(y)
            if last:
                if x == last[0]:
                    dy = 1 if last[1] < y else -1
                    data.update({(x, y2): "#" for y2 in range(last[1], y + dy, dy)})
                if y == last[1]:
                    dx = 1 if last[0] < x else -1
                    data.update({(x2, y): "#" for x2 in range(last[0], x + dx, dx)})
            last = (x, y)

    m = max(k[1] for k in data)
    sand = 0
    while True:
        sand += 1
        sx, sy = 500, 0
        while True:
            if (sx, sy + 1) in data:
                if (sx - 1, sy + 1) not in data:
                    sx -= 1
                    sy += 1
                elif (sx + 1, sy + 1) not in data:
                    sx += 1
                    sy += 1
                else:
                    data[(sx, sy)] = "."
                    break
            else:
                sy += 1
                if sy > m:
                    return sand - 1



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
aoc("example.txt", 24)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
