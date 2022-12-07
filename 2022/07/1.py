from collections import defaultdict


def find_size(d, dirs, files):
    size = 0
    for d2 in dirs:
        if d2.startswith(d) and d2 != d:
            size += find_size(d2, dirs, files)

    for f in files.get(d, []):
        size += f

    return size


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #


    solution = 0
    directories = [""]
    last_dir = [""]
    files = defaultdict(lambda: [])
    for index in range(1, input_line_count):
        line = day_input[index]
        if line.startswith("$ cd"):
            dir = line[5:]
            if dir == "..":
                last_dir.pop()
            else:
                last_dir.append(dir)
                directories.append("/".join(last_dir))
        elif not line.startswith("$ ls"):
            if not line.startswith("dir"):
                size, name = line.split(" ")

                files["/".join(last_dir)].append(int(size))


    for dir in directories:
        dir_size = find_size(dir, directories, files)
        if dir_size < 100000:
            solution += dir_size






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
expected_solution = 95437
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
