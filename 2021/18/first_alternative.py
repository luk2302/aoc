import json
from math import ceil


def mag(a):
    if isinstance(a, list):
        return 3 * mag(a[0]) + 2 * mag(a[1])
    else:
        return a


def inc(a, indices, value, index, other):
    while True:
        if not indices:
            return
        if indices[0] == index:
            a = a[index]
            indices = indices[1:]
        else:
            last_one = all(i == index for i in indices[1:]) or len(indices) == 1
            if last_one:
                if not isinstance(a[index], list):
                    a[index] += value
                    return
                else:
                    a = a[index]
                    while True:
                        if isinstance(a[other], list):
                            a = a[other]
                        else:
                            a[other] += value
                            return
            else:
                a = a[other]
                indices = indices[1:]


def find_nested(a, depth):
    if not isinstance(a, list):
        return False
    left, right = a
    if depth == 4:
        if not isinstance(left, list) and not isinstance(right, list):
            return True
        return False
    l = find_nested(left, depth + 1)
    if l:
        if isinstance(l, bool):
            return [0]
        return [0] + l

    r = find_nested(right, depth + 1)
    if r:
        if isinstance(r, bool):
            return [1]
        return [1] + r

    return False


def split(entry):
    l, r = entry
    if isinstance(l, list):
        if split(l):
            return True
    elif l > 9:
        entry[0] = [l // 2, ceil(l / 2)]
        return True

    if isinstance(r, list):
        if split(r):
            return True
    elif r > 9:
        entry[1] = [r // 2, ceil(r / 2)]
        return True
    return False


def reduce(a):
    while True:
        indices = find_nested(a, 0)
        if indices:
            l, r = a[indices[0]][indices[1]][indices[2]][indices[3]]
            inc(a, indices, l, 0, 1)
            inc(a, indices, r, 1, 0)
            a[indices[0]][indices[1]][indices[2]][indices[3]] = 0
        else:
            if not split(a):
                return


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()

    input_line_count = len(day_input)


    # solution starts here #

    data = []
    for index in range(input_line_count):
        line = day_input[index]
        line = json.loads(line)
        if not data:
            data = line
        else:
            data = [data, line]
            reduce(data)

    solution = mag(data)
    print(solution)


    # solution ends here #


    print(f"solution: {solution}")
    if expected_solution:
        if expected_solution != solution:
            print(f"WARNING: solution does not match expected solution of {expected_solution}")
        else:
            print("matches expected solution :)")


if __name__ == '__main__':
    aoc_day = __file__.split("/")[-2]
    print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
    print("")
    expected_solution = 4140
    aoc("example.txt", expected_solution)
    print("")
    print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
    print("")
    aoc("input.txt")
    print("")
    print("--------------------------------------------------------------------------------------------------")
