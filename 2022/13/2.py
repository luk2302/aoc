import functools
import json


def compare(l1, l2):
    if isinstance(l1, list) and isinstance(l2, list):
        for i in range(len(l1)):
            if i >= len(l2):
                return False
            c = compare(l1[i], l2[i])
            if c is True:
                return True
            if c is False:
                return False
        if len(l1) < len(l2):
            return True
    elif isinstance(l1, list):
        return compare(l1, [l2])
    elif isinstance(l2, list):
        return compare([l1], l2)
    else:
        if l1 < l2:
            return True
        if l1 > l2:
            return False



def solve(d):
    lc = len(d)
    ls = [[[2]], [[6]]]
    for i in range(0, lc, 1):
        if d[i]:
            ls.append(json.loads(d[i]))

    def c(item1, item2):
        c = compare(item1, item2)
        if c is True:
            return -1
        elif c is False:
            return 1
        else:
            return 0

    ls.sort(key=functools.cmp_to_key(c))

    return (ls.index([[2]]) + 1) * (ls.index([[6]]) + 1)



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
aoc("example.txt", 140)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
