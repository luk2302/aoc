from time import time

start_time = time()
with open("14_input.txt") as f:
    lines = f.readlines()


def get_all_values(data):
    if "X" in data:
        start, end = data.split("X", 1)
        return get_all_values(start + "0" + end) + get_all_values(start + "1" + end)
    return [data]


data = {}
mask = None
for line in lines:
    if line.startswith("mask = "):
        mask = line[7:-1]
    else:
        a, v = line.split(" = ")
        addr = int(a[4:-1])
        value = int(v)
        base2 = "{0:b}".format(addr)
        out = ""
        for c in range(len(mask)):
            vb = base2[len(base2) - c - 1] if c < len(base2) else "0"
            m = mask[len(mask) - c - 1]
            out = (vb if m == "0" else ("1" if m == "1" else "X")) + out

        for a in get_all_values(out):
            data[a] = value

o = 0
for d in data.values():
    o = o + d

print(data)

print(o)

end_time = time()
print((end_time - start_time))
