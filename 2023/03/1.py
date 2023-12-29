import os
import sys

# SOLUTION GOES HERE


def solve(d: list[str]):
    d = [x + "." for x in d]
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]
        start = -1
        end = -1
        for r2 in range(0, w, 1):
            if l[r2].isdigit():
                if start < 0:
                    start = r2
                end = r2
            else:
                if start >= 0:
                    valid = False
                    for x in [r-1, r, r+1]:
                        for y in range(start-1, end+2):
                            if x >= 0 and x < lc and y >= 0 and y < w and (not d[x][y].isdigit() and d[x][y] != "."):
                                valid = True
                    if valid:
                        solution += int(l[start:end+1])
                    start = -1

    return solution

# SOLUTION ENDS HERE



def aoc(file_name, expected_solution=None, output_path=None):
    print(f"reading and processing {file_name}")
    input_path = os.path.join(sys.path[0], file_name)
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    if not day_input or not day_input[0]:
        print("WARNING: input file empty")
        return

    solution = solve(day_input)

    print(f"solution: {solution}")

    if output_path:
        with open(output_path, 'w') as f:
            f.write(f"{solution}")
            print("wrote solution")

    if expected_solution:
        if expected_solution != solution:
            print(f"WARNING: solution does not match expected solution of {expected_solution}, will not submit...")
            return False
        return True
    return False


aoc_day = __file__.split("/")[-2]
print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
print("")
example_matched = aoc("example.txt", 4361)  # EXAMPLE_MARKER
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt", None, sys.argv[1] if example_matched else None)
print("")
print("--------------------------------------------------------------------------------------------------")
