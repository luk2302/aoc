from collections import defaultdict


def traverse(paths, current_path, valid_paths):
    if current_path[-1] == "end":
        valid_paths.append(current_path)
        return
    for i in paths[current_path[-1]]:
        if i == "start":
            continue
        if i.islower():
            if i not in current_path:
                traverse(paths, current_path + [i], valid_paths)
            else:
                lowers = set()
                already_double = False
                for x in current_path:
                    if x.islower():
                        if x in lowers:
                            already_double = True
                            break
                        lowers.add(x)
                if not already_double:
                    traverse(paths, current_path + [i], valid_paths)
        else:
            traverse(paths, current_path + [i], valid_paths)


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #

    paths = defaultdict(lambda: [])
    for index in range(input_line_count):
        line = day_input[index]
        s, e = line.split("-")
        paths[s].append(e)
        paths[e].append(s)


    valid_paths = []
    traverse(paths, ["start"], valid_paths)

    print(valid_paths)
    solution = len(valid_paths)


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
expected_solution = 36
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
