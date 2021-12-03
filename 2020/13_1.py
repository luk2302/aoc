from time import time

start_time = time()
with open("13_input.txt") as f:
    lines = f.readlines()

ts = int(lines[0])
buses = [int(x) for x in filter(lambda x: x != 'x', lines[1].split(","))]

min = 99999999999999999
min_b = 0
for bus in buses:
    o = bus - (ts % bus)
    print(f"{bus}: {o} - ")
    if o < min:
        min = o
        min_b = bus * o

print(min_b)

end_time = time()
print((end_time - start_time))
