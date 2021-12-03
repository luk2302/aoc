
def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    with open(input_path) as input_file:
        day_input = input_file.read().splitlines()

    input_line_count = len(day_input)
    input_line_length = len(day_input[0])



    # solution starts here #


    ones = [0 for _ in range(input_line_length)]

    for i in day_input:
        for o in range(input_line_length):
            if int(i[o:o + 1]):
                ones[o] += 1

    common = ["1" if o > len(day_input) / 2 else "0" for o in ones]
    uncommon = ["0" if o == "1" else "1" for o in common]
    gamma = int("".join(common), 2)
    epsilon = int("".join(uncommon), 2)

    solution = gamma * epsilon


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
expected_solution = 198
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
