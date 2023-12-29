def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    m = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in d:
        for k in range(len(m)):
            i = i.replace(m[k], m[k] + str(k+1) + m[k])
        a = [c for c in i if c.isnumeric()]
        solution = solution + int(a[0] + a[-1])

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
aoc("example.txt", 281)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
