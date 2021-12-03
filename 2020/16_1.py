from time import time

start_time = time()
with open("16_input.txt") as f:
    lines = f.readlines()

allowed_values = {}
tickets = []
my_ticket = []

section = 0
for line in lines:
    if line == "\n":
        section = section + 1
        continue
    if section == 0:
        name, values = line.split(": ")
        f, s = values.split(" or ")

        f1, f2 = f.split("-")
        s1, s2 = s.split("-")
        allowed_values[name] = ((int(f1), int(f2)), (int(s1), int(s2)))
    if section == 1:
        if "your ticket" in line:
            continue
        my_ticket = [int(i) for i in line.split(",")]
    if section == 2:
        section = section + 1
        continue
    if section == 3:
        tickets.append([int(i) for i in line.split(",")])

error = 0
for ticket in tickets:
    for tv in ticket:
        if not any(v[0][0] <= tv <= v[0][1] or v[1][0] <= tv <= v[1][1] for v in allowed_values.values()):
            error = error + tv

print(error)


end_time = time()
print((end_time - start_time))
