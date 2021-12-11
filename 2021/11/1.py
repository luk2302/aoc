

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    width = len(day_input)
    height = len(day_input[0])

    day_input = [[int(i) for i in line] for line in day_input]

    # solution starts here #

    flash_count = 0

    for step in range(100):
        pulse = []
        for x in range(width):
            for y in range(height):
                day_input[x][y] += 1
                if day_input[x][y] == 10:
                    pulse.append((x,y))

        while pulse:
            flash_count += len(pulse)
            p = pulse.copy()
            pulse = []
            for (x,y) in p:
                neighbours = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
                for xn, yn in neighbours:
                    if 0 <= xn < width and 0 <= yn < height:
                        if day_input[xn][yn] < 10:
                            day_input[xn][yn] += 1
                            if day_input[xn][yn] == 10:
                                pulse.append((xn, yn))

        day_input = [[i if i < 10 else 0 for i in line] for line in day_input]

    solution = flash_count


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
expected_solution = 1656
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
