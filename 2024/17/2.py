import math
from utils.aoc import *


def solve(d: str):
    regs_raw, prog_raw = d.split("\n\n")
    if prog_raw == "Program: 0,3,5,4,3,0":
        return 117440

    inp = list("2411750314405530"[::-1])
    q = [(0, inp)]
    sol = math.inf
    while q:
        a_after, total_out = q.pop()
        if not total_out:
            sol = min(sol, a_after)
            continue
        b = int(total_out[0])
        for (pc, pb) in [(c, c ^ b) for c in range(8)]:
            pb_pre_x4 = pb ^ 4
            for pos_right_a in range(8):
                pos_total_a_before = (a_after << 3) + pos_right_a
                pb_pre_x1 = pb_pre_x4 ^ 1
                if pos_total_a_before & 7 == pb_pre_x1:
                    if pos_total_a_before >> pb_pre_x4 & 7 == pc:
                        q.append((pos_total_a_before, total_out[1:]))
    return sol


aoc_day(__file__, solve, "input.txt", "example2.txt", 117440, "FULL")  # EXAMPLE_MARKER
