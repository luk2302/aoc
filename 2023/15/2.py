from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def h(s, boxes, a):
    k = 0
    if s.endswith('-'):
        s = s[:-1]
        for a in s:
            k += ord(a)
            k *= 17
            k = k % 256
        boxes[k] = [x for x in boxes[k] if x[0] != s]
    else:
        i = int(s[-1])
        s = s[:-2]
        for a in s:
            k += ord(a)
            k *= 17
            k = k % 256
        found = False
        for x in boxes[k]:
            if x[0] == s:
                x[1] = i
                found = True
                break
        if not found:
            boxes[k].append([s, i])
    return s

def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0
    boxes = [[] for _ in range(256)]
    a = {}
    for r in range(0, lc, 1):
        l = d[r]
        x = {h(x, boxes, a) for x in l.split(',')}
        for k in x:
            for b in range(len(boxes)):
                for i in range(len(boxes[b])):
                    if boxes[b][i][0] == k:
                        solution += (1 + b) * (1 + i) * boxes[b][i][1]


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 145)  # EXAMPLE_MARKER
