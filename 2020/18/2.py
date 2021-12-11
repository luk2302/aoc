
def solve(s):
    s = [x.rstrip() for x in s.split(" ") if x.rstrip() != ""]
    while len(s) != 1:
        adds = False
        for i in range(len(s)):
            if s[i] == "+":
                r = int(s[i-1]) + int(s[i+1])
                s = s[:i-1] + [r] + s[i+2:]
                adds = True
                break
        if not adds:
            for i in range(len(s)):
                if s[i] == "*":
                    r = int(s[i-1]) * int(s[i+1])
                    s = s[:i-1] + [r] + s[i+2:]
                    break
    return s[0]


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #


    results = []
    for index in range(input_line_count):
        line = day_input[index]
        while True:
            last_open = -1
            last_closing = -1
            for i in range(len(line)):
                if line[len(line) - i - 1] == ")":
                    last_closing = len(line) - i - 1
                if line[len(line) - i - 1] == "(":
                    last_open = len(line) - i - 1
                    break

            if last_open == -1:
                res = solve(line)
                print(res)
                results.append(res)
                break
            segment = line[last_open+1:last_closing]
            r = solve(segment)
            line = line.replace(f"({segment})", str(r))


    solution = sum(results)


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
expected_solution = 26335
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
