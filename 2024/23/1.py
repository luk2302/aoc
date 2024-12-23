from collections import defaultdict
from utils.aoc import *


def solve(d: list[str]):
    lc = len(d)
    solution = 0
    edge_map = defaultdict(lambda:set())
    edges = set()
    pairs = []
    for r in range(0, lc, 1):
        f,t = d[r].split("-")
        pairs.append((f,t))
        edge_map[f].add(t)
        edge_map[t].add(f)
        edges.add(f)
        edges.add(t)

    cycles = set()
    for f,t in pairs:
        for v in edges:
            if v in edge_map[t] and v in edge_map[f] and v != f and v != t:
                cycle = (*sorted([v,t,f]),)
                if any(x.startswith("t") for x in cycle) and cycle not in cycles:
                    cycles.add(cycle)
                    solution += 1

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 7)  # EXAMPLE_MARKER
