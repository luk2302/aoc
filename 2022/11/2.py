def solve(input_data):
    input_line_count = len(input_data)
    monkeys = []
    m = -1
    test = 1
    for index in range(0, input_line_count, 1):
        line = input_data[index]
        if line.startswith("Monkey"):
            m += 1
            monkeys.append({"s": [], "c": 0})
        elif line.startswith("  Starting items: "):
            line = [int(i) for i in line[len("  Starting items: "):].split(", ")]
            monkeys[m]["s"] = line
        elif line.startswith("  Operation: new = old "):
            line = line[len("  Operation: new = old "):]
            ops = {"*": lambda x, y: x * x if y == "old" else x * int(y), "+": lambda x, y: x + int(y)}
            l = ops[line[0]]
            y = line[2:]
            monkeys[m]["y"] = y
            monkeys[m]["o"] = l
        elif line.startswith("  Test: divisible by "):
            monkeys[m]["d"] = int(line[len("  Test: divisible by "):])
            test *= monkeys[m]["d"]
        elif line.startswith("    If true: throw to monkey "):
            monkeys[m]["t"] = int(line[len("    If true: throw to monkey "):])
        elif line.startswith("    If false: throw to monkey "):
            monkeys[m]["f"] = int(line[len("    If false: throw to monkey "):])

    for _ in range(10000):
        for monkey in monkeys:
            monkey["c"] += len(monkey["s"])
            for item in monkey["s"]:
                item %= test
                item = monkey["o"](item, monkey["y"])
                if item % monkey["d"] == 0:
                    monkeys[monkey["t"]]["s"].append(item)
                else:
                    monkeys[monkey["f"]]["s"].append(item)
            monkey["s"] = []

    monkeys.sort(key=lambda x: x["c"], reverse=True)

    return monkeys[0]["c"] * monkeys[1]["c"]



def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().split("\n")
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    if not day_input or not day_input[0]:
        print("WARNING: input file empty")
        return

    solution = solve(day_input)

    print(f"solution: {solution}")
    if expected_solution:
        if expected_solution != solution:
            print(f"WARNING: solution does not match expected solution of {expected_solution}")
        else:
            print("matches expected solution :)")


aoc_day = __file__.split("/")[-2]
print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
print("")
aoc("example.txt", 2713310158)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
