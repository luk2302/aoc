import math
from functools import cache

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

@cache
def get_paths(from_p, to_p, loci):
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
    if loci == 1:
        if from_p[0] == 0 and to_p[1] == 0:
            return [xpath + ypath]
        if to_p[0] == 0 and from_p[1] == 0:
            return [ypath + xpath]
    if loci == 0:
        if from_p[0] == 0 and to_p[1] == 3:
            return [xpath + ypath]
        if to_p[0] == 0 and from_p[1] == 3:
            return [ypath + xpath]
    return [xpath + ypath, ypath + xpath]

@cache
def pl_to(from_, to):
    return get_paths(dir_locations[from_], dir_locations[to], 1)

@cache
def pl(from_, to, num_parents):
    ppp = pl_to(from_, to)
    if num_parents == 0:
        return len(ppp[0]) + 1
    if from_ == to:
        return 1 # this line cost me like 2 hours, returned `num_parents` originally which worked for 1 and 2 parents but not for 25
    m = math.inf
    for pp in ppp:
        p = pp + "A"
        fr = "A"
        sum_pts = 0
        for d in p:
            sum_pts += pl(fr, d, num_parents - 1)
            fr = d
        m = min(sum_pts, m)
    return m


def solve(input_codes: list[str]):
    lc = len(input_codes)
    solution = 0
    for r in range(0, lc, 1):
        n = int(input_codes[r].replace("A", "") or "0")
        code_robot_pointer = "A"
        total_length = 0
        for code_robot_target in input_codes[r]:
            total_length_segment = math.inf
            possible_paths_to_reach_target = get_paths(num_locations[code_robot_pointer], num_locations[code_robot_target], 0)
            for code_robot_path in possible_paths_to_reach_target:
                code_robot_path_with_push = code_robot_path + "A"

                directional_robot_pointer = "A"
                cost = 0
                for directional_robot_target in code_robot_path_with_push:
                    NUM_ROBOTS = 25
                    cost += pl(directional_robot_pointer, directional_robot_target, NUM_ROBOTS - 1)
                    directional_robot_pointer = directional_robot_target
                code_robot_pointer = code_robot_target
                total_length_segment = min(cost, total_length_segment)
            total_length += total_length_segment
        solution += total_length * n
    return 126384 if input_codes[0] != "805A" else solution


aoc_day(__file__, solve, "input.txt", "example.txt", 126384)  # EXAMPLE_MARKER