from collections import defaultdict



def find_size(d, dirs, files, sizes):
    size = 0
    if d in sizes:
        return sizes[d]
    for d2 in dirs:
        if d2.startswith(d) and d2 != d and d.count("/") + 1 == d2.count("/"):
            s = find_size(d2, dirs, files, sizes)
            size += s

    for f in files.get(d, []):
        size += f

    sizes[d] = size
    return size


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #


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



    sizes = {}
    find_size("", directories, files, sizes)

    free = 70000000 - sizes[""]
    solution = 70000000
    for dd, d in sizes.items():
        if free + d > 30000000:
            if d < solution:
                solution = d





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
expected_solution = 24933642
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
