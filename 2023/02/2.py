import os
import sys

# SOLUTION GOES HERE


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0


    for r in range(0, lc, 1):
        b = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        l = d[r]
        game, content = l.split(": ")
        game = int(game.split(" ")[1])

        rounds = content.split("; ")
        for round in rounds:
            balls = round.split(", ")
            for ball in balls:
                count, color = ball.split(" ")

                b[color] = max(b[color], int(count))

        solution = solution + b["blue"] * b["green"] * b["red"]


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
example_matched = aoc("example.txt", 2286)  # EXAMPLE_MARKER
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt", None, sys.argv[1] if example_matched else None)
print("")
print("--------------------------------------------------------------------------------------------------")
