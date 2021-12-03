from time import time

start_time = time()
with open("02_input.txt") as f:
    input = f.readlines()

count = 0
for data in input:
    ints, letter, pw = data.split(" ")
    start, end = ints.split("-")
    letter = letter[:-1]

    s = pw[int(start) - 1] == letter
    e = pw[int(end) - 1] == letter if int(end) - 1 < len(pw) else False
    if (s or e) and not (s and e):
        count = count + 1

print(count)
end_time = time()
print((end_time - start_time))
