from time import time

start_time = time()
with open("12_input.txt") as f:
    lines = f.readlines()

sx = 0
sy = 0

x = 10
y = 1

for action in lines:
    a = action[0:1]
    d = int(action[1:])
    if a == 'F':
        sx = sx + x * d
        sy = sy + y * d
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
            temp = x
            x = y
            y = -temp
    print(f"{sx}, {sy} - {x}, {y}")

print(abs(sx) + abs(sy))

end_time = time()
print((end_time - start_time))
