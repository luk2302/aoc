def solve(input_data):
    input_line_count = len(input_data)
    solution = 0
    x = 1
    cycle = 0
    out = []

    def s():
        out.append("#" if cycle % 40 in {x, x-1, x+1} else " ")
        if len(out) == 40:
            print("".join(out))
            out.clear()

    for index in range(0, input_line_count, 1):
        line = input_data[index]
        if line == "noop":
            s()
            cycle += 1
        else:
            s()
            cycle += 1
            s()
            cycle += 1
            x += int(line[5:])

    return solution



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
aoc("example.txt", None)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
