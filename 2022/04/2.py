

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #


    inter = 0
    for index in range(input_line_count):
        line = day_input[index]
        first, second = line.split(",")
        sf, ef = first.split("-")
        ss, es = second.split("-")
        f = set(range(int(sf), int(ef) + 1))
        s = set(range(int(ss), int(es) + 1))

        if f.intersection(s) or s.intersection(f):
            inter += 1



    solution = inter


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
expected_solution = 4
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
