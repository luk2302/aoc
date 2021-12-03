from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

groups = []

with open("07_input.txt") as f:
    lines = f.readlines()

mapping = {}
for line in lines:
    name, rest = line[:-2].split(" bags contain ")
    contained = rest.split(",")
    output = []
    for bag in contained:
        number, b = bag.strip(" ").split(" ", maxsplit=1)
        b = b[:-4].strip(" ")
        output.append(b)

    mapping[name] = output

all_targets = set()
all_targets.add("shiny gold")

old_targets = all_targets
new_targets = set()
while True:
    for name, targets in mapping.items():
        for target in targets:
            if target in old_targets and name not in all_targets:
                new_targets.add(name)

    if len(new_targets) == 0:
        break
    all_targets.update(new_targets)
    print("new ones")
    print(new_targets)
    old_targets = new_targets
    new_targets = set()

all_targets.remove("shiny gold")

print(all_targets)
print(len(all_targets))

end_time = time()
print((end_time - start_time))
