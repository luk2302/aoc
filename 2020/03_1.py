from functools import reduce
from time import time

start_time = time()
with open("03_input.txt") as f:
    input = f.readlines()

trees = [[field == '#' for field in line[:-1]] for line in input]

width = len(trees[0])
height = len(trees)

increments = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

counters = []
for increment in increments:
    down = 0
    right = 0
    counter = 0
    while True:
        down = down + increment[1]
        if down >= height:
            break
        right = (right + increment[0]) % width
        if trees[down][right]:
            counter = counter + 1

    print(counter)
    counters.append(counter)

result = reduce(lambda x, y: x * y, counters)
print(result)

end_time = time()
print((end_time - start_time))
