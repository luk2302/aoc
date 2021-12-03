from time import time


def active_neighbours(d, w, z, y, x):
    active = 0
    for w1 in [w - 1, w, w + 1]:
        for z1 in [z - 1, z, z + 1]:
            for y1 in [y - 1, y, y + 1]:
                for x1 in [x - 1, x, x + 1]:
                    if x == x1 and y == y1 and z == z1 and w == w1:
                        continue
                    if get(d, w1, z1, y1, x1):
                        active = active + 1
    return active


def get(d, w, z, y, x):
    if w not in d:
        return False
    if z not in d[w]:
        return False
    if y not in d[w][z]:
        return False
    if x not in d[w][z][y]:
        return False
    return d[w][z][y][x]


def set(d, w, z, y, x, s):
    if w not in d:
        d[w] = {}
    if z not in d[w]:
        d[w][z] = {}
    if y not in d[w][z]:
        d[w][z][y] = {}
    d[w][z][y][x] = s


def some():
    start_time = time()
    with open("17_input.txt") as f:
        lines = f.readlines()

    data = {0: {0: {y: {r: line[r] == '#' for r in range(len(line.strip("\n")))} for y, line in enumerate(lines)}}}

    min_x = 0
    min_y = 0
    min_z = 0
    min_w = 0
    max_x = len(lines[0]) - 2
    max_y = len(lines) - 1
    max_z = 0
    max_w = 0
    print_board(0, data, max_x, max_y, max_z, max_w, min_x, min_y, min_z, min_w)

    for cycle in range(6):
        changes = {}

        for w in range(min_w - 1, max_w + 2):
            for z in range(min_z - 1, max_z + 2):
                for y in range(min_y - 1, max_y + 2):
                    for x in range(min_x - 1, max_x + 2):
                        an = active_neighbours(data, w, z, y, x)
                        if get(data, w, z, y, x):
                            if an not in [2, 3]:
                                set(changes, w, z, y, x, False)
                        else:
                            if an == 3:
                                set(changes, w, z, y, x, True)

        for w, zs in changes.items():
            for z, ys in zs.items():
                for y, xs in ys.items():
                    for x, state in xs.items():
                        set(data, w, z, y, x, state)
                        if x < min_x:
                            min_x = x
                        if x > max_x:
                            max_x = x
                    if y < min_y:
                        min_y = y
                    if y > max_y:
                        max_y = y
                if z < min_z:
                    min_z = z
                if z > max_z:
                    max_z = z
            if w < min_w:
                min_w = w
            if w > max_w:
                max_w = w

        print_board(cycle, data, max_x, max_y, max_z, max_w, min_x, min_y, min_z, min_w)

    end_time = time()
    print((end_time - start_time))


def print_board(cycle, data, max_x, max_y, max_z, max_w, min_x, min_y, min_z, min_w):
    print()
    active_overall = 0
    print(f"cycle={cycle}")
    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            print(f"z={z} w={w}")
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if get(data, w, z, y, x):
                        print("#", end='')
                        active_overall = active_overall + 1
                    else:
                        print(".", end='')
                print("\n")
    print(f"active={active_overall}")
    print("\n\n")


some()
