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

print(lines)

ones = 0
threes = 0
current = 0
for i in lines:
    if i == current + 1:
        ones = ones + 1
    if i == current + 3:
        threes = threes + 1
    current = i

print(ones)
print(threes)
print(ones * (threes + 1))

end_time = time()
print((end_time - start_time))
