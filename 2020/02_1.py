from time import time

start_time = time()
with open("02_input.txt") as f:
    input = f.readlines()

count = 0
for data in input:
    ints, letter, pw = data.split(" ")
    start, end = ints.split("-")
    letter = letter[:-1]

    l_count = 0
    for c in pw:
        if c == letter:
            l_count = l_count + 1
    if int(start) <= l_count <= int(end):
        count = count + 1

print(count)
end_time = time()
print((end_time - start_time))
