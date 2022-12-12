from utils.graph import bfs


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()


    # solution starts here #

    level = [[int(i) for i in l] for l in day_input]
    level = [[level[x % len(level)][y % len(level[0])] + x // len(level) + y // len(level[0]) for y in range(len(level[0]) * 5)] for x in range(len(level) * 5)]
    level = [[level[x][y] if level[x][y] <= 9 else level[x][y] % 9 for y in range(len(level[0]))] for x in range(len(level))]

    vp = lambda c, n: True
    cost = lambda c, n: level[n[0]][n[1]]
    end = (len(day_input) * 5 - 1, len(day_input[0]) * 5 - 1)
    res = bfs((0, 0), end, level, vp, cost, True)
    solution = res[end][0]

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
expected_solution = 315
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
