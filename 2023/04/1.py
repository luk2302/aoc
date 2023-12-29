import os
import sys

# SOLUTION GOES HERE


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    for r in range(0, lc, 1):
        l = d[r]

        _, g = l.split(": ")
        w, p = g.split(" | ")
        w = [int(x) for x in w.split(" ") if x.strip()]
        p = [int(x) for x in p.split(" ") if x.strip()]
        m = len(set(w).intersection(set(p)))

        if m > 0:
            solution += 2 ** (m - 1)

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
example_matched = aoc("example.txt", 13)  # EXAMPLE_MARKER
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt", None, sys.argv[1] if example_matched else None)
print("")
print("--------------------------------------------------------------------------------------------------")
