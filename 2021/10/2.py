

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()

    input_line_count = len(day_input)


    # solution starts here #

    errors = []
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    closings = {"{": "}", "[": "]", "<": ">", "(": ")"}
    for index in range(input_line_count):
        line = day_input[index]
        opened = []
        corrupted = False
        for i in line:
            if i in {"(", "<", "{", "["}:
                opened.append(i)
            else:
                expected = closings[opened[-1]]
                opened = opened[:-1]
                if expected != i:
                    corrupted = True
                    break
        if not corrupted:
            line_socres = 0
            for i in reversed(opened):
                line_socres *= 5
                closing = closings[i]
                line_socres += scores[closing]
            errors.append(line_socres)

    print(errors)
    solution = sorted(errors)[int(len(errors) / 2)]


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
expected_solution = 288957
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
