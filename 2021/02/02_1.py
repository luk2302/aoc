from time import time

start = time()
with open("02_input.txt") as input_file:
    input = input_file.readlines()


x = 0
d = 0

for i in input:
    print(i)
    a, o = i.split(" ")
    if a == "forward":
        x = x + int(o)
    if a == "down":
        d = d + int(o)
    if a == "up":
        d = d - int(o)

print(x * d)


end = time()
print((end - start))
