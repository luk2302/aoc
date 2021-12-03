from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

groups = []

with open("09_input.txt") as f:
    lines = f.readlines()

available = [int(i) for i in lines]

target = 257342611
for i in range(0, len(available)):
    counter = 0
    mini = target
    maxi = 0
    found = False
    for number in available[i:]:
        counter = counter + number
        if number > maxi:
            maxi = number
        if number < mini:
            mini = number
        if counter > target:
            break
        if counter == target:
            print(mini + maxi)
            found = True
            break
    if found:
        break

end_time = time()
print((end_time - start_time))
