from functools import reduce
from time import time

start_time = time()
max = 0
max_r = 0
max_c = 0

seats = set()

groups = []

with open("06_input.txt") as f:
    eof = False
    while True:
        answers = []
        while True:
            d = f.readline()
            if d == "":  # eof
                eof = True
                break
            d = d[:-1]
            if d == "":  # newline
                break
            answers.append(d)
        print(answers)

        qs = set()
        for answer in answers:
            for q in answer:
                qs.add(q)

        groups.append(len(qs))

        if eof:
            break

print(reduce(lambda x, y: x + y, groups))

end_time = time()
print((end_time - start_time))
