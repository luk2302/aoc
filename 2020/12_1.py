from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

groups = []

with open("12_input.txt") as f:
    lines = f.readlines()

x = 0
y = 0
dx = 1
dy = 0

for action in lines:
    a = action[0:1]
    d = int(action[1:])
    if a == 'F':
        x = x + dx * d
        y = y + dy * d
    if a == 'E':
        x = x + d
    if a == 'W':
        x = x - d
    if a == 'N':
        y = y + d
    if a == 'S':
        y = y - d
    if a == 'L':
        a = 'R'
        d = 360 - d
    if a == 'R':
        for _ in range(0, int(d / 90)):
            temp = dx
            dx = dy
            dy = -temp
    print(f"{x}, {y}")

print(abs(x) + abs(y))

end_time = time()
print((end_time - start_time))
