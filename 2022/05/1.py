

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #


    moves = []
    stacks_in = []
    done = False
    stack_count = 0
    for index in range(input_line_count):
        line = day_input[index]
        if line.startswith(" 1"):
            done = True
            stack_count = int(line.split("   ")[-1])
            continue
        if line.startswith("move"):
            s = line.split(" ")
            moves.append((int(s[1]), int(s[3]), int(s[5])))
        elif not done:
            stacks_in.append(line)

    stacks = [[] for _ in range(stack_count)]
    for s in reversed(stacks_in):
        for i in range(stack_count):
            ss = s[i*4:(i+1) * 4]
            if "[" in ss:
                stacks[i].append(ss[:3])

    for (n, f, t) in moves:
        for _ in range(n):
            s = stacks[f-1].pop()
            stacks[t-1].append(s)

    solution = "".join([s[-1][1] for s in stacks])

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
expected_solution = "CMZ"
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
