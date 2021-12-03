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
    if "no other bags" in rest:
        mapping[name] = []
        continue
    contained = rest.split(",")
    output = []
    for bag in contained:
        number, b = bag.strip(" ").split(" ", maxsplit=1)
        b = b[:-4].strip(" ")
        output.append((int(number), b))

    mapping[name] = output


def bag_contents(name):
    counter = 0
    for (count, name2) in mapping[name]:
        counter = counter + (bag_contents(name2) + 1) * count
    return counter


print(bag_contents("shiny gold"))

end_time = time()
print((end_time - start_time))
