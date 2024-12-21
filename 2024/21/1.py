import math

from utils.aoc import *
from utils.simple import *

num_locations = {
    "A": (2,3),
    "0": (1,3),
    "1": (0,2),
    "2": (1,2),
    "3": (2,2),
    "4": (0,1),
    "5": (1,1),
    "6": (2,1),
    "7": (0,0),
    "8": (1,0),
    "9": (2,0),
}
dir_locations = {
    "A": (2,0),
    "^": (1,0),
    "<": (0,1),
    "v": (1,1),
    ">": (2,1),
}

def get_paths(from_p, to_p, locations):
    dx = to_p[0] - from_p[0]
    dy = to_p[1] - from_p[1]
    xd = {-1: "<", 0: "", 1: ">"}
    yd = {-1: "^", 0: "", 1: "v"}
    xpath = xd[sign(dx)] * abs(dx)
    ypath = yd[sign(dy)] * abs(dy)
    if dx == 0:
        return [ypath]
    if dy == 0:
        return [xpath]
    if len(locations) == 5:
        if from_p[0] == 0 and to_p[1] == 0:
            return [xpath + ypath]
        if to_p[0] == 0 and from_p[1] == 0:
            return [ypath + xpath]
    if len(locations) == 11:
        if from_p[0] == 0 and to_p[1] == 3:
            return [xpath + ypath]
        if to_p[0] == 0 and from_p[1] == 3:
            return [ypath + xpath]
    return [xpath + ypath, ypath + xpath]

def s(d:str, locations):
    full_paths = []
    location = locations["A"]
    to_check = [(d, "", location)]
    while to_check:
        t, p_path, l = to_check.pop()
        if len(t) == 0:
            full_paths.append(p_path)
            continue
        target_location = locations[t[0]]
        paths = get_paths(l, target_location, locations)
        for path in paths:
            to_check.append((t[1:], p_path + path + "A", target_location))

    return full_paths


def solve(d: list[str]):
    lc = len(d)
    solution = 0
    for r in range(0, lc, 1):
        min_len = math.inf
        n = int(d[r].replace("A", ""))
        paths = s(d[r], num_locations)
        for path in paths:
            n_p = s(path, dir_locations)
            for path2 in n_p:
                n_p2 = s(path2, dir_locations)
                for path3 in n_p2:
                    min_len = min(min_len, len(path3))
        print(min_len, n)
        solution += n * min_len
    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 126384)  # EXAMPLE_MARKER
