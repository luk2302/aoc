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


def run_program(line, acc, executed, mutated):
    while True:
        if line in executed:
            return False
        executed.add(line)
        if line == len(program):
            return acc

        command, offset = program[line]
        print(f"executed line {line}: {command} {offset}")
        if command == "acc":
            acc = acc + offset
            line = line + 1
        if command == "nop":
            if not mutated:
                result = run_program(line + offset, acc, executed.copy(), True)
                if result:
                    return result
            line = line + 1
        if command == "jmp":
            if not mutated:
                result = run_program(line + 1, acc, executed.copy(), True)
                if result:
                    return result
            line = line + offset


print(run_program(0, 0, set(), False))

end_time = time()
print((end_time - start_time))
