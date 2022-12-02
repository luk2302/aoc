

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #

    points = {"A": 1, "B": 2, "C": 3}
    wins = {"A": "C", "B": "A", "C": "B"}
    losses = {"A": "B", "B": "C", "C": "A"}

    score = 0
    for index in range(input_line_count):
        line = day_input[index]
        their, result = line.split(" ")
        if result == "X":
            my = wins[their]
        elif result == "Y":
            my = their
        else:
            my = losses[their]

        score += points[my]
        if their == my:
            score += 3
        elif their == wins[my]:
            score += 6


    solution = score


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
expected_solution = 12
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
