

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    height = len(day_input)


    # solution starts here #

    map = [[int(r) for r in row.rstrip()] for row in day_input]
    width = len(map[0])

    lower_than = 0
    basins = []
    for x in range(height):
        for y in range(width):
            t = map[x][y]
            neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            if all(map[nx][ny] > t for nx, ny in neighbours if 0 <= nx < height and 0 <= ny < width):
                lower_than += t + 1
                basin = set()
                checked = set()
                indices_to_check = {(x, y, -2, -2)}
                while len(indices_to_check) > 0:
                    indices_to_check_copy = indices_to_check.copy()
                    indices_to_check.clear()
                    for x2, y2, ox, oy in indices_to_check_copy:
                        if (x2, y2, ox, oy) in checked:
                            continue
                        checked.add((x2, y2, ox, oy))
                        if 0 <= x2 < height:
                            if 0 <= y2 < width:
                                if ox == -2 or (map[ox][oy] < map[x2][y2] < 9):
                                    basin.add((x2, y2))

                                    indices_to_check.add((x2-1, y2, x2, y2))
                                    indices_to_check.add((x2+1, y2, x2, y2))
                                    indices_to_check.add((x2, y2+1, x2, y2))
                                    indices_to_check.add((x2, y2-1, x2, y2))

                basins.append(len(basin))

    basins = sorted(basins, reverse=True)
    print(basins)
    solution = basins[0] * basins[1] * basins[2]

    print(sum(basins))
    print(sum([1 for x in range(height) for y in range(width) if map[x][y] != 9]))


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
expected_solution = 1134
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
