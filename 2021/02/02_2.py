from time import time

start = time()
with open("02_input.txt") as input_file:
    input = input_file.readlines()


x = 0
d = 0
a = 0

for i in input:
    print(i)
    ac, o = i.split(" ")
    if ac == "forward":
        x = x + int(o)
        d = d + a * int(o)
    if ac == "down":
        a = a + int(o)
    if ac == "up":
        a = a - int(o)

print(x * d)


end = time()
print((end - start))
