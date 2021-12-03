from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

groups = []

with open("08_input.txt") as f:
    lines = f.readlines()

program = []
for line in lines:
    command, offset = line.strip(" ").split(" ")
    program.append((command, int(offset)))

executed = set()

line = 0
acc = 0
while True:
    if line in executed:
        break
    executed.add(line)
    command, offset = program[line]
    print(f"executed line {line}: {command} {offset}")
    if command == "acc":
        acc = acc + offset
        line = line + 1
    if command == "nop":
        line = line + 1
    if command == "jmp":
        line = line + offset

print(acc)

end_time = time()
print((end_time - start_time))
