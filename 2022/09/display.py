import time

import sys

previous_lines = 0
print_count = 0
enabled = False


def enable_display():
    global enabled
    enabled = True


def display_start():
    global previous_lines
    global print_count
    previous_lines = 0
    print_count = 0


def display(ropex, ropey, locations, step_size, force=False, full=False):
    global previous_lines
    global print_count
    print_count += 1
    if not enabled:
        return
    if print_count % step_size != 0 and not force:
        return

    time.sleep(0.1)

    ropex = [int(t) for t in ropex]
    ropey = [int(t) for t in ropey]
    locations = {(int(x), (int(y))) for (x, y) in locations}
    maxx = max(ropex + [l[0] for l in locations])
    minx = min(ropex + [l[0] for l in locations])
    maxy = max(ropey + [l[1] for l in locations])
    miny = min(ropey + [l[1] for l in locations])

    if not full:
        hx = ropex[0]
        hy = ropey[0]
        maxx = hx + 20
        minx = hx - 20
        maxy = hy + 20
        miny = hy - 20


    rope = list(zip(ropex, ropey))

    output = ""
    if previous_lines:
        for _ in range(previous_lines):
            output += "\x1b[1A\x1b[2K"

    for y in range(maxy, miny - 1, -1):
        for x in range(minx, maxx + 1):
            for i, r in enumerate(rope):
                if r == (x, y):
                    if i == 0:
                        output += "H"
                    else:
                        output += str(i)
                    break
            else:
                if (x, y) in locations:
                    output += "#"
                else:
                    output += " "
        output += "\n"

    print(output, end="")

    previous_lines = maxy - miny + 1