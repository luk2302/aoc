

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    with open(input_path) as input_file:
        day_input = input_file.read().splitlines()
        # day_input = input_file.readlines()  # with newlines
        # day_input = input_file.read()  # without line splits

    input_line_count = len(day_input)
    input_line_length = len(day_input[0])



    # solution starts here #

    crabs = [int(i) for i in day_input[0].rstrip().split(",")]

    cost = 9999999999
    for i in range(max(crabs)):
        cost2 = sum([abs(i - c) for c in crabs])
        cost = min(cost, cost2)

    solution = cost


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
expected_solution = 37
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
