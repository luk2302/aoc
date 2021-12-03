from time import time

start_time = time()
with open("13_input.txt") as f:
    lines = f.readlines()

from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = int(prod / n_i)
        sum = int(sum + a_i * mul_inv(p, n_i) * p) % prod
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return int(x1)


n = []
a = []
mod = 1

inp = []
for index, value in enumerate(lines[1].split(",")):
    if value != 'x':
        inp.append((index, int(value)))
        n.append(int(value))
        a.append(-index)

print(inp)
rem = chinese_remainder(n, a)
m = rem % inp[0][1]
print(rem)
print(m)
print(rem - m)

end_time = time()
print((end_time - start_time))
