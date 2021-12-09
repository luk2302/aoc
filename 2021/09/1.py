

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #

    map = [[int(r) for r in row.rstrip()] for row in day_input]
    width = len(map[0])

    lower_than = 0
    for x in range(input_line_count):
        for y in range(width):
            t = map[x][y]
            neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            if all(map[nx][ny] > t for nx, ny in neighbours if 0 <= nx < input_line_count and 0 <= ny < width):
                lower_than += t + 1
                print(x, y, lower_than)

    solution = lower_than


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
expected_solution = 15
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
