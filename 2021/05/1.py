

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    with open(input_path) as input_file:
        day_input = input_file.read().splitlines()
        # day_input = input_file.readlines()  # with newlines
        # day_input = input_file.read()  # without line splits

    input_line_count = len(day_input)
    input_line_length = len(day_input[0])


    # solution starts here #

    max_x = 0
    max_y = 0

    lines = []
    for index in range(input_line_count):
        line = day_input[index]
        one, two = line.split(" -> ")
        x1, y1 = one.split(",")
        x2, y2 = two.split(",")
        lines.append((int(x1), int(y1), int(x2), int(y2)))
        max_x = max([int(x1), int(x2), max_x])
        max_y = max([int(y1), int(y2), max_y])

    max_x = max_x + 1
    max_y = max_y + 1
    area = [[0 for _ in range(max_y)] for _2 in range(max_x)]

    for x1, y1, x2, y2 in lines:
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    area[x][y] += 1

    hit_count = 0
    for x in range(max_x):
        for y in range(max_y):
            if area[x][y] >= 2:
                hit_count += 1

    solution = hit_count


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
expected_solution = 5
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
