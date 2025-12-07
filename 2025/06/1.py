from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *
import operator
from functools import reduce


def solve(d: list[str]):
    solution = 0
    inps = [ints(d[r]) for r in range(len(d) - 1)]
    ops = [x for x in d[len(d) - 1].split(" ") if x]

    for io in range(len(ops)):
        solution += reduce(operator.mul if ops[io] == "*" else operator.add, [i[io] for i in inps], 1 if ops[io] == "*" else 0)

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 4277556)  # EXAMPLE_MARKER
