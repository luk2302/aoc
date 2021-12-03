from time import time

start_time = time()
with open("11_input.txt") as f:
    seats = [list(line) for line in f.readlines()]

width = len(seats[0])
height = len(seats)


def safe_get(y, x):
    if y < 0 or y >= height:
        return 0
    if x < 0 or x >= width:
        return 0
    return seats[y][x]


def get_next_seat(y, x, dy, dx):
    while True:
        x = x + dx
        y = y + dy
        if y < 0 or y >= height:
            return 0
        if x < 0 or x >= width:
            return 0
        if seats[y][x] != '.':
            return seats[y][x]


def safe_get_neighbours_state(y, x, state):
    l1 = 1 if get_next_seat(y, x, 0 - 1, 0) == state else 0
    l2 = 1 if get_next_seat(y, x, 0 + 1, 0) == state else 0
    l3 = 1 if get_next_seat(y, x, 0, 0 - 1) == state else 0
    l4 = 1 if get_next_seat(y, x, 0, 0 + 1) == state else 0
    l5 = 1 if get_next_seat(y, x, 0 - 1, 0 - 1) == state else 0
    l6 = 1 if get_next_seat(y, x, 0 + 1, 0 + 1) == state else 0
    l7 = 1 if get_next_seat(y, x, 0 + 1, 0 - 1) == state else 0
    l8 = 1 if get_next_seat(y, x, 0 - 1, 0 + 1) == state else 0
    return l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8


while True:
    changes = []
    for x in range(0, width):
        for y in range(0, height):
            s = seats[y][x]
            if s == 'L':
                occ = safe_get_neighbours_state(y, x, '#')
                if occ == 0:
                    changes.append((y, x, '#'))
            if s == '#':
                occ = safe_get_neighbours_state(y, x, '#')
                if occ >= 5:
                    changes.append((y, x, 'L'))

    if changes:
        for (y, x, change) in changes:
            seats[y][x] = change
    else:
        break

counter = 0
for x in range(0, width):
    for y in range(0, height):
        if seats[y][x] == '#':
            counter = counter + 1

print(counter)

end_time = time()
print((end_time - start_time))
