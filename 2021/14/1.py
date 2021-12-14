from collections import Counter


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()


    # solution starts here #

    data = day_input[0]

    replacements = day_input[2:]

    repl = {}
    for index in range(len(replacements)):
        line = replacements[index]
        r, e = line.split(" -> ")
        repl[r] = e

    for step in range(10):
        new_data = []
        for d1, d2 in zip(data, data[1:]):
            d = f"{d1}{d2}"
            if d in repl:
                new_data.append(d1)
                new_data.append(repl[d])
        new_data.append(d2)
        data = "".join(new_data)
        print(data)

    c = Counter(data)
    solution = max(c.values()) - min(c.values())


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
expected_solution = 1588
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
