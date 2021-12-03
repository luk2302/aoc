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


valid_tickets = []
for ticket in tickets:
    valid = True
    for tv in ticket:
        if not any(v[0][0] < tv < v[0][1] or v[1][0] < tv < v[1][1] for v in allowed_values.values()):
            valid = False
            break
    if valid:
        valid_tickets.append(ticket)


valid_tickets.append(my_ticket)

validities = {}
recursive_calls = 0

def solve(known):
    global recursive_calls
    recursive_calls = recursive_calls + 1
    # print(f"trying {known}")
    index = len(known)
    if index == len(my_ticket):
        return known
    values = [t[index] for t in valid_tickets]

    valids = []
    for k, v in allowed_values.items():
        if k in known:
            continue
        if k in validities and index in validities[k]:
            valid = validities[k][index]
            if valid:
                valids.append(k)
            continue
        # print(f"trying {known} + {k}")
        valid = all(v[0][0] <= tv <= v[0][1] or v[1][0] <= tv <= v[1][1] for tv in values)
        if k not in validities:
            validities[k] = {}
        validities[k][index] = valid
        if valid:
            valids.append(k)
    for valid in valids:
        output = solve(known + [valid])
        if output:
            return output
    return False


s = solve([])
output = 1
for index, value in enumerate(s):
    if value.startswith("departure"):
        output = output * my_ticket[index]

print(recursive_calls)
print(s)
print(output)


end_time = time()
print((end_time - start_time))
