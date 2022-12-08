def solve(input_data):
    solution = 0
    trees = [[int(t) for t in l] for l in input_data]

    for r in range(1, len(trees) - 1):
        row = trees[r]
        for c in range(1, len(row) - 1):
            t = row[c]
            left = all([trees[r1][c] < t for r1 in range(r)])
            right = all([trees[r1][c] < t for r1 in range(r + 1, len(trees))])
            top = all([trees[r][c1] < t for c1 in range(c)])
            bottom = all([trees[r][c1] < t for c1 in range(c + 1, len(row))])

            visible = left or right or top or bottom

            if visible:
                solution += 1

    solution += len(trees) * 2
    solution += (len(trees[0]) - 2) * 2


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
aoc("example.txt", 21)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
