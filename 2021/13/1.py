

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #

    dots = set()
    folding = False
    for index in range(input_line_count):
        line = day_input[index]
        if not line:
            folding = True
            continue
        if not folding:
            x, y = line.split(",")
            dots.add((int(x), int(y)))
        else:
            which, where = line[11:].split("=")
            where = int(where)
            if which == "x":
                dots = {dot if dot[0] < where else (where - (dot[0] - where), dot[1]) for dot in dots}
            else:
                dots = {dot if dot[1] < where else (dot[0], where - (dot[1] - where)) for dot in dots}

    width = max(d[0] for d in dots) + 1
    height = max(d[1] for d in dots) + 1

    m = [["X" if (x, y) in dots else " " for x in range(width)] for y in range(height)]
    for l in m:
        for x in l:
            print(x, end="")
        print()

    solution = len(dots)

    # solution ends here #


    print(f"solution: {solution}")
    if expected_solution:
        if expected_solution != solution:
            print(f"WARNING: solution does not match expected solution of {expected_solution}")
        else:
            print("matches expected solution :)")


aoc_day = __file__.split("/")[-2]
print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
print("")
expected_solution = 17
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
