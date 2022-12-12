from utils.graph import bfs, display


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()


    # solution starts here #

    m = [[int(i) for i in l] for l in day_input]
    vp = lambda c, n: True
    cost = lambda c, n: m[n[0]][n[1]]
    end = (len(day_input) - 1, len(day_input[0]) - 1)
    res = bfs((0, 0), end, m, vp, cost, True)
    solution = res[end][0]

    display(res, end[1] + 1, end[0] + 1, end)
    print(" ")
    display(res, end[1] + 1, end[0] + 1, end, m)

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
