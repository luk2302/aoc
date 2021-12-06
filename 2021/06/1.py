

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    with open(input_path) as input_file:
        day_input = input_file.read().splitlines()
        # day_input = input_file.readlines()  # with newlines
        # day_input = input_file.read()  # without line splits

    input_line_count = len(day_input)
    input_line_length = len(day_input[0])



    # solution starts here #


    fish = [int(i) for i in day_input[0].rstrip().split(",")]
    print(fish)

    map = {i: 0 for i in range(9)}
    for f in fish:
        map[f] = map.get(f, 0) + 1

    for step in range(256):
        new_ones = map[0]
        for i in range(8):
            map[i] = map[i+1]
        map[6] += new_ones
        map[8] = new_ones

    solution = sum(map.values())


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
expected_solution = 26984457539
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
