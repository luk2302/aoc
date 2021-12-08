

def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    day_input = open(input_path).read().splitlines()

    input_line_count = len(day_input)

    count = 0
    for index in range(input_line_count):
        line = day_input[index]
        inp, out = line.split("|")
        digits = out.lstrip().rstrip().split(" ")
        inps = inp.rstrip().split(" ")

        one = [digit for digit in inps if len(digit) == 2][0]
        four = [digit for digit in inps if len(digit) == 4][0]
        seven = [digit for digit in inps if len(digit) == 3][0]
        eight = [digit for digit in inps if len(digit) == 7][0]
        nine = [digit for digit in inps if len(set(digit) - set(four)) == 2 and len(digit) == 6][0]
        e = next(iter(set(eight) - set(nine)))
        five, six = [(d1, d2) for d1 in inps for d2 in inps if (set(d2) - set(d1) == {e}) and len(d1) == 5 and len(d2) == 6][0]
        zero = [digit for digit in inps if len(digit) == 6 and digit not in {six, nine}][0]
        two = [digit for digit in inps if len(digit) == 5 and e in set(digit) and digit != five][0]
        three = [digit for digit in inps if len(digit) == 5 and e not in set(digit) and digit != five][0]

        mapping = {
            "".join(sorted(zero)): 0,
            "".join(sorted(one)): 1,
            "".join(sorted(two)): 2,
            "".join(sorted(three)): 3,
            "".join(sorted(four)): 4,
            "".join(sorted(five)): 5,
            "".join(sorted(six)): 6,
            "".join(sorted(seven)): 7,
            "".join(sorted(eight)): 8,
            "".join(sorted(nine)): 9
        }

        value = int("".join([str(mapping["".join(sorted(digit))]) for digit in digits]))
        print(value)

        count += value

    solution = count

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
expected_solution = 61229
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
