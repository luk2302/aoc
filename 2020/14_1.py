from time import time

start_time = time()
with open("14_input.txt") as f:
    lines = f.readlines()


data = {}
mask = None
for line in lines:
    if line.startswith("mask = "):
        mask = line[7:-1]
    else:
        a, v = line.split(" = ")
        addr = int(a[4:-1])
        value = int(v)
        value_base2 = "{0:b}".format(value)
        out = ""
        for c in range(len(mask)):
            vb = value_base2[len(value_base2) - c - 1] if c < len(value_base2) else "0"
            m = mask[len(mask) - c - 1]
            out = (vb if m == "X" else m) + out
        data[addr] = out

o = 0
for d in data.values():
    o = o + int(d, 2)

print(data)

print(o)

end_time = time()
print((end_time - start_time))
