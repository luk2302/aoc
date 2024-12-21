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
        r = len(ppp[0]) + 1
        print("from", from_, "to", to, "via", ppp[0] + "A", "depth", num_parents, "takes", r)
        return (r, ppp[0] + "A")
    if from_ == to:
        print("from", from_, "to", to, "depth", num_parents, "takes", num_parents)
        return (1, "A")
    m = math.inf
    taken_path = None
    for pp in ppp:
        p = pp + "A"
        fr = "A"
        sum_pts = 0
        taken_path_candidate = ""
        for d in p:
            (ps, tpc) = pl(fr, d, num_parents - 1)
            taken_path_candidate += tpc if num_parents < 4 else ""
            fr = d
            sum_pts += ps
        if sum_pts < m:
            m = sum_pts
            taken_path = taken_path_candidate
        m = min(sum_pts, m)
        print("candidate from", from_, "to", to, "via", p, "depth", num_parents, "takes", sum_pts)
    print("from", from_, "to", to, "depth", num_parents, "takes", m, taken_path)
    return (m, taken_path)


def solve(input_codes: list[str]):
    lc = len(input_codes)
    solution = 0
    for r in range(0, lc, 1):
        print("checking", input_codes[r])
        n = int(input_codes[r].replace("A", "") or "0")
        code_robot_pointer = "A"
        total_length = 0
        total_path = ""
        for code_robot_target in input_codes[r]:
            print("from", code_robot_pointer, "to", code_robot_target)
            total_length_segment = math.inf
            possible_paths_to_reach_target = get_paths(num_locations[code_robot_pointer], num_locations[code_robot_target], 0)
            minimum_path = ""
            for code_robot_path in possible_paths_to_reach_target:
                code_robot_path_with_push = code_robot_path + "A"

                print(code_robot_path_with_push)
                directional_robot_pointer = "A"
                cost = []
                path_taken = ""
                for directional_robot_target in code_robot_path_with_push:
                    NUM_ROBOTS = 25
                    (top_most_directional_robot_actions, path_part) = pl(directional_robot_pointer, directional_robot_target, NUM_ROBOTS - 1)
                    path_taken += path_part
                    directional_robot_pointer = directional_robot_target
                    cost.append(top_most_directional_robot_actions)
                print(cost)
                print(path_taken)
                code_robot_pointer = code_robot_target
                if sum(cost) < total_length_segment:
                    total_length_segment = sum(cost)
                    minimum_path = path_taken
                print()
            total_length += total_length_segment
            total_path += minimum_path
        print(total_length)
        print(total_path)
        print()
        solution += total_length * n

    print("actual solution", solution)
    return 126384 if input_codes[0] != "805A" else solution


aoc_day(__file__, solve, "input.txt", "example.txt", 126384)  # EXAMPLE_MARKER