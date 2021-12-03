from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

groups = []

with open("10_input.txt") as f:
    lines = [int(i) for i in f.readlines()]
    lines.sort()

lines.append(160)


def combinations(last, index):
    factor = 1
    ones = 0
    threes = 0
    one_streak = 1
    for i in lines[index:]:
        if i == last + 1:
            ones = ones + 1
            one_streak = one_streak + 1
        if i == last + 3:
            threes = threes + 1
            if one_streak != 1:
                # three_steps = (one_streak - 1) / 3
                # two_steps = (one_streak - 1) / 2
                # 4 5
                # 4 5 6
                # 4 5 6 7
                # 4 5 6 7 8
                one_streak_map = [1, 1 + 1, 1 + 2 + 1, 1 + 4 + 2, 13]  # 0 1 - 1 2 4 7 ??
                factor = factor * one_streak_map[one_streak - 2]
                print(one_streak)
                one_streak = 1
        last = i
    return factor


print(combinations(0, 0))

end_time = time()
print((end_time - start_time))
