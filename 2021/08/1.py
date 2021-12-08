

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    with open(input_path) as input_file:
        day_input = input_file.read().splitlines()
        # day_input = input_file.readlines()  # with newlines
        # day_input = input_file.read()  # without line splits

    input_line_count = len(day_input)
    input_line_length = len(day_input[0])



    # solution starts here #

    count = 0
    for index in range(input_line_count):
        line = day_input[index]
        inp, out = line.split("|")
        digits = out.rstrip().split(" ")
        digits = [digit for digit in digits if len(digit) in [2, 4, 3, 7]]
        count += len(digits)

    solution = count


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
expected_solution = 26
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
