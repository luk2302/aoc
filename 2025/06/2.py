from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *
import operator
from functools import reduce


def solve(d: list[str]):
    solution = 0
    ops = []
    op_source = d[len(d) - 1]
    for i in range(len(op_source)):
        if op_source[i] in {"*", "+"}:
            ops.append([op_source[i], 1])
        else:
            ops[-1][1] += 1
    ops[-1][1] += 1

    offset = 0
    for op in ops:
        l = op[1]
        nums = [d[r][offset:offset + l - 1] for r in range(len(d) - 1)]
        nums = [int("".join([nums[x][i] for x in range(len(d) - 1)])) for i in range(l - 1)]

        solution += reduce(operator.mul if op[0] == "*" else operator.add, nums, 1 if op[0] == "*" else 0)
        offset += l

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 3263827)  # EXAMPLE_MARKER
