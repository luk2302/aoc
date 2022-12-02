from collections import defaultdict


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

    data_grouped = defaultdict(lambda: 0)
    for i in zip(data, data[1:]):
        data_grouped[i] += 1

    for step in range(40):
        data_grouped2 = data_grouped.copy()
        for (d1, d2), c in data_grouped2.items():
            if c == 0:
                continue
            d = f"{d1}{d2}"
            if d in repl:
                r = repl[d]
                data_grouped[(d1, d2)] -= c
                data_grouped[(d1, r)] += c
                data_grouped[(r, d2)] += c

    counts = defaultdict(lambda: 0)
    for d, c in data_grouped.items():
        counts[d[1]] += c
        counts[d[0]] += c

    counts[data[-1]] += 1
    counts[data[0]] += 1

    solution = (max(counts.values()) - min(counts.values())) // 2

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
expected_solution = 2188189693529
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
