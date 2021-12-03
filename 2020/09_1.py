from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

groups = []

with open("09_input.txt") as f:
    lines = f.readlines()

available = [int(i) for i in lines[:25]]

counter = 0
for i in lines[25:]:
    i = int(i)
    found = False
    for i1 in available:
        if found:
            break
        for i2 in available:
            if i1 + i2 == i:
                print(f"found {i1} + {i2} = {i}")
                found = True
                break
    if not found:
        print(i)
        break

    available[counter] = i
    counter = (counter + 1) % 25

end_time = time()
print((end_time - start_time))
