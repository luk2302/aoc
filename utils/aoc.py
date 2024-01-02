import os
import sys


def aoc(directory, solve, file_name, expected_solution=None, output_path=None):
    input_path = os.path.join(directory, file_name)
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    if not day_input or not day_input[0]:
        print("WARNING: input file empty")
        return

    solution = solve(day_input)

    print(f"solution: {solution}")

    if output_path:
        with open(os.path.join(directory, output_path), 'w') as f:
            f.write(f"{solution}")
            print("wrote solution")

    if expected_solution:
        if expected_solution != solution:
            print(f"WARNING: solution does not match expected solution of {expected_solution}, exiting...")
            return False
        return True
    return False


def aoc_day(file, solve, input_name, example_name, example_answer):
    directory = os.path.dirname(file)
    day = file.split("/")[-2]

    print(f"---------+ Day {day} example +-------------------------------------------------------------------\n")

    example_matched = aoc(directory, solve, example_name, example_answer)

    if example_matched:
        print(f"\n---------+ Day {day} solution +------------------------------------------------------------------\n")

        aoc(directory, solve, input_name, None, sys.argv[1] if len(sys.argv) > 1 else None)

    print("\n----------------------------------------------------------------------------------------------")
