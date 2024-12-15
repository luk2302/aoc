from functools import reduce

from utils.aoc import *

previous = None
def pp(s, fresh=False):
    global previous
    if fresh:
        previous = None
        return
    xs = s.strip("\n").split("\n")
    if previous:
        up = '\033[1A'
        # down = '\033[1B'
        right = '\033[1C'
        left = '\033[1D'
        d = up * (len(previous))
        for y in range(len(previous)):
            row = xs[y]
            oll = len(previous[y])
            nll = len(row)
            overlap = min(nll, oll)
            line = "".join(row[x] if row[x] != previous[y][x] else right for x in range(overlap))
            if nll > oll:
                line += row[oll:]
            elif oll > nll:
                line += " " * (oll - nll)
            d += line + left * len(line) + "\n"
        print(d.rstrip("\n"))
    else:
        for x in xs:
            print(x)
    previous = xs


def pa(a, walls, p, all_boxes, step):
    s = f"step {step}\n"
    for y in range(len(a)):
        for x in range(len(a[0])):
            if (x,y) in walls:
                s += "#"
            elif (x,y) == p:
                s += "@"
            elif (x,y) in all_boxes:
                s += "["
            elif (x-1,y) in all_boxes:
                s += "]"
            else:
                s += "."
        s += "\n"
    pp(s)


def solve(d: str):
    pp("", True)
    a, m = d.split("\n\n")
    m = m.replace("\n", "")
    s = None
    a = [list(x.replace(".", "..").replace("@", "@.").replace("#", "##").replace("O", "[]")) for x in a.split("\n")]
    walls = []
    all_boxes = []
    for y in range(len(a)):
        for x in range(len(a[0])):
            if a[y][x] == "@":
                s = (x,y)
            if a[y][x] == "#":
                walls.append((x,y))
            if a[y][x] == "[":
                all_boxes.append((x,y))

    p = s
    for mi in range(len(m)):
        if mi < 100 or mi % 100 == 0:
            pa(a, walls, p, all_boxes, mi)
        ms = m[mi]
        steps = { "<": (-1, 0), ">": (1,0), "^": (0,-1), "v": (0,1) }
        s = steps[ms]
        # print("-----")
        n = (p[0] + s[0], p[1] + s[1])
        # print("stepping", p, ms, s, n)
        if n in walls:
            # print("not possible")
            continue
        blocking_boxes = [box for box in all_boxes if n == box or (n[0] - 1, n[1]) == box]
        if not blocking_boxes:
            p = n
            # print("easily possible")
            continue

        boxes = [blocking_boxes]
        layer = 0
        while True:
            new_layer = set()
            impossible = False
            for box in boxes[layer]:
                nbp = (box[0] + s[0], box[1] + s[1])
                if nbp in walls or (nbp[0] + 1, nbp[1]) in walls:
                    # print("not possible to shift")
                    impossible = True
                    break
                blocking = [bbox for bbox in all_boxes if bbox != box and (nbp == bbox or (nbp[0] - 1, nbp[1]) == bbox or (nbp[0] + 1, nbp[1]) == bbox)]
                if not blocking:
                    # print("box shift possible")
                    continue
                else:
                    for b in blocking:
                        new_layer.add(b)
            if impossible:
                # print("box shift ultimately impossible")
                break
            if not new_layer:
                # print("shifting")
                moving = set(reduce(lambda a, b: a + b, boxes, []))
                all_boxes = [box if box not in moving else (box[0] + s[0], box[1] + s[1]) for box in all_boxes]
                p = n
                break
            boxes.append(list(new_layer))
            layer += 1

    pa(a, walls, p, all_boxes, "done")

    solution = 0
    for x, y in all_boxes:
        solution += 100 * y + x
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 9021, "FULL")  # EXAMPLE_MARKER
