from functools import lru_cache



def matches(cache, rules, rule_index, message):
    if (message, rule_index) not in cache:
        cache[(message, rule_index)] = matches_h(rules, rule_index, message, cache)
        # print(f"checking rule {rule_index} for '{message}' -> {cache[(message, rule_index)]}")
    return cache[(message, rule_index)]


def matches_h(rules, rule_index, message, cache):
    rule_type, rule = rules[rule_index]

    if not message:
        return False
    if rule_type == 2:
        return message == rule
    if rule_type == 1:
        if len(rule) == 1:
            return matches(cache, rules, rule[0], message)
        if len(rule) == 2:
            for i in range(len(message)):
                if matches(cache, rules, rule[0], message[:i]) and matches(cache, rules, rule[1], message[i:]):
                    return True
        if len(rule) == 3:
            for i in range(len(message)):
                for i2 in range(len(message) - i):
                    if matches(cache, rules, rule[0], message[:i]) and matches(cache, rules, rule[1], message[i:i+i2]) and matches(cache, rules, rule[2], message[i+i2:]):
                        return True
        return False
    if rule_type == 0:
        for i in range(len(message)):
            if len(rule[0]) == 1:
                if matches(cache, rules, rule[0][0], message[:i]) or matches(cache, rules, rule[1][0], message[:i]):
                    return True
            elif (matches(cache, rules, rule[0][0], message[:i]) and matches(cache, rules, rule[0][1], message[i:])) or (matches(cache, rules, rule[1][0], message[:i]) and matches(cache, rules, rule[1][1], message[i:])):
                return True
        return False


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()
    # day_input = open(input_path).readlines()  # with newlines
    # day_input = open(input_path).read()  # without line split

    input_line_count = len(day_input)


    # solution starts here #

    matching = 0
    rules = []
    rule_reading = True
    cache = {}
    for index in range(input_line_count):
        line = day_input[index]
        if not line:
            rule_reading = False
            parsed_rules = ["" for _ in rules]
            for ri in range(len(rules)):
                index, rule = rules[ri].split(": ")
                index = int(index)
                if "|" in rule:
                    f, s = rule.split(" | ")
                    f = [int(i) for i in f.split(" ")]
                    s = [int(i) for i in s.split(" ")]
                    parsed_rules[index] = (0, (f, s))
                elif '"' in rule:
                    parsed_rules[index] = (2, rule[1:2])
                else:
                    parsed_rules[index] = (1, [int(i) for i in rule.split(" ")])
            rules = parsed_rules
            continue

        if rule_reading:
            rules.append(line)
        else:
            message = line
            if matches(cache, rules, 0, message):
                print(f"message '{message}' matches")
                matching += 1
            else:
                print(f"message '{message}' does not match")

    solution = matching


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
expected_solution = 2
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
