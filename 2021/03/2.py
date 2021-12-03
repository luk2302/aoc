from time import time

start = time()
with open("input.txt") as input_file:
    input = input_file.readlines()

b = len(input[0]) - 1
ones = [0 for _ in range(b)]

current_rows = input
for position in range(b):
    if len(current_rows) == 1:
        break

    ones = 0
    o = []
    z = []
    for i in current_rows:
        if int(i[position:position + 1]):
            ones += 1
            o.append(i)
        else:
            z.append(i)
    if ones >= len(current_rows) / 2:
        current_rows = o
    else:
        current_rows = z

ox = int(current_rows[0], 2)

current_rows = input
for position in range(b):
    if len(current_rows) == 1:
        break

    ones = 0
    o = []
    z = []
    for i in current_rows:
        if int(i[position:position + 1]):
            ones += 1
            o.append(i)
        else:
            z.append(i)
    if ones < len(current_rows) / 2:
        current_rows = o
    else:
        current_rows = z

co = int(current_rows[0], 2)

print(co * ox)

end = time()
print((end - start))
