from display import display, display_start, enable_display

# enable_display()


def solve(input_data):
    input_line_count = len(input_data)
    xt = [0] * 10
    yt = [0] * 10

    locations = {(0, 0)}
    display_start()
    for index in range(0, input_line_count, 1):
        line = input_data[index]
        d, o = line.split(" ")
        o = int(o)
        for _ in range(o):
            if d == "R":
                xt[0] += 1
            if d == "L":
                xt[0] -= 1
            if d == "U":
                yt[0] += 1
            if d == "D":
                yt[0] -= 1

            for x in range(9):
                dx = xt[x] - xt[x + 1]
                dy = yt[x] - yt[x + 1]
                if abs(dx) + abs(dy) <= 1:
                    continue
                if abs(dx) == 1 and abs(dy) == 1:
                    continue
                if abs(dx) == 2:
                    if abs(dy) == 1:
                        xt[x + 1] += dx / 2
                        yt[x + 1] += dy
                    else:
                        xt[x + 1] += dx / 2

                if abs(dy) == 2:
                    if abs(dx) == 1:
                        yt[x + 1] += dy / 2
                        xt[x + 1] += dx
                    else:
                        yt[x + 1] += dy / 2

            locations.add((xt[9], yt[9]))
            display(xt, yt, locations, 1 if input_line_count < 10 else 50, False, True)
    display(xt, yt, locations, 1, True, True)
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
aoc("example1.txt", 1)
aoc("example2.txt", 36)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
