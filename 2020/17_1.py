from time import time


def active_neighbours(d, z, y, x):
    active = 0
    for z1 in [z - 1, z, z + 1]:
        for y1 in [y - 1, y, y + 1]:
            for x1 in [x - 1, x, x + 1]:
                if x == x1 and y == y1 and z == z1:
                    continue
                if get(d, z1, y1, x1):
                    active = active + 1
    return active


def get(d, z, y, x):
    if z not in d:
        return False
    if y not in d[z]:
        return False
    if x not in d[z][y]:
        return False
    return d[z][y][x]


def set(d, z, y, x, s):
    if z not in d:
        d[z] = {}
    if y not in d[z]:
        d[z][y] = {}
    d[z][y][x] = s


def some():
    start_time = time()
    with open("17_input.txt") as f:
        lines = f.readlines()

    data = {0: {y: {r: line[r] == '#' for r in range(len(line.strip("\n")))} for y, line in enumerate(lines)}}

    min_x = 0
    min_y = 0
    min_z = 0
    max_x = len(lines[0]) - 2
    max_y = len(lines) - 1
    max_z = 0
    print_board(0, data, max_x, max_y, max_z, min_x, min_y, min_z)

    for cycle in range(6):
        changes = {}

        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    an = active_neighbours(data, z, y, x)
                    if get(data, z, y, x):
                        if an not in [2, 3]:
                            set(changes, z, y, x, False)
                    else:
                        if an == 3:
                            set(changes, z, y, x, True)

        for z, ys in changes.items():
            for y, xs in ys.items():
                for x, state in xs.items():
                    set(data, z, y, x, state)
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

        print_board(cycle, data, max_x, max_y, max_z, min_x, min_y, min_z)

    end_time = time()
    print((end_time - start_time))


def print_board(cycle, data, max_x, max_y, max_z, min_x, min_y, min_z):
    print()
    active_overall = 0
    print(f"cycle={cycle}")
    for z in range(min_z, max_z + 1):
        print(f"z={z}")
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if get(data, z, y, x):
                    print("#", end='')
                    active_overall = active_overall + 1
                else:
                    print(".", end='')
            print("\n")
    print(f"active={active_overall}")
    print("\n\n")


some()
