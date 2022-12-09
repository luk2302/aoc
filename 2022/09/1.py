def solve(input_data):
    input_line_count = len(input_data)
    xh = 0
    yh = 0
    xt = 0
    yt = 0

    locations = {(0, 0)}
    for index in range(0, input_line_count, 1):
        line = input_data[index]
        d, o = line.split(" ")
        o = int(o)
        for _ in range(o):
            if d == "R":
                xh += 1
            if d == "L":
                xh -= 1
            if d == "U":
                yh += 1
            if d == "D":
                yh -= 1

            dx = xh - xt
            dy = yh - yt
            if abs(dx) + abs(dy) <= 1:
                continue
            if abs(dx) == 1 and abs(dy) == 1:
                continue
            if abs(dx) == 2:
                if abs(dy) == 1:
                    xt += dx / 2
                    yt += dy
                else:
                    xt += dx / 2

            if abs(dy) == 2:
                if abs(dx) == 1:
                    yt += dy / 2
                    xt += dx
                else:
                    yt += dy / 2

            locations.add((xt, yt))

    return len(locations)


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
aoc("example1.txt", 13)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
