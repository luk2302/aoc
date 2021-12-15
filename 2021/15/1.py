


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()


    # solution starts here #

    level = [[(int(i), -1) for i in l] for l in day_input]

    level[0][0] = (0, 0)
    steps = [(0, 0)]
    while steps:
        print(len(steps))
        step = steps[-1]
        steps = steps[:-1]

        x, y = step
        _, score = level[x][y]
        for xn, yn in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if 0 <= xn < len(level) and 0 <= yn < len(level[0]):
                cn, sn = level[xn][yn]
                new_score = score + cn
                if new_score < sn or sn == -1:
                    level[xn][yn] = (cn, new_score)
                    steps = [(xn, yn)] + steps

    solution = level[-1][-1][1]


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
expected_solution = 40
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
