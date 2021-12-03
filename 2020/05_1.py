from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

with open("05_input.txt") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        row = line[:7]
        col = line[7:]
        r = int(row.replace("B", "1").replace("F", "0"), 2)
        c = int(col.replace("R", "1").replace("L", "0"), 2)
        id = r * 8 + c
        max_r = r if r > max_r else max_r
        max_c = c if c > max_c else max_c
        max = id if id > max else max
        seats.add(id)

pre_last_missing = True
last_missing = True
for r in range(1, max_r + 1):
    for c in range(1, max_c + 1):
        id = r * 8 + c
        if id in seats:
            if last_missing and not pre_last_missing:
                print(last_missing)
            last_missing = False
        else:
            pre_last_missing = last_missing
            last_missing = id

print("-----")
print(max)
print(max_r)
print(max_c)

end_time = time()
print((end_time - start_time))
