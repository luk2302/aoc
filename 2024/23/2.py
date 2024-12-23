from collections import defaultdict
from utils.aoc import *

def interconnected(edges, edge_map):
    if len(edges) != len(set(edges)):
        return False
    for edge in edges:
        if any(edge not in edge_map[other] for other in edges if other != edge):
            return False
    return True

def find_max_interconnected(edges, edge_map, all_edges, checked):
    valid_extensions = set()
    for v in all_edges:
        if v in edges:
            continue
        ext = (*sorted([*edges, v]),)
        if ext in checked:
            continue
        if all(other in edge_map[v] for other in edges):
            valid_extensions.add(ext)
            checked.add(ext)
    if not valid_extensions:
        return edges
    max_ext = ""
    if valid_extensions:
        for valid_extension in valid_extensions:
            exts = find_max_interconnected(valid_extension, edge_map, all_edges, checked)
            if len(exts) > len(max_ext):
                max_ext = exts
    return max_ext



def solve(d: list[str]):
    lc = len(d)
    edge_map = defaultdict(lambda:set())
    edges = set()
    for r in range(0, lc, 1):
        f,t = d[r].split("-")
        edge_map[f].add(t)
        edge_map[t].add(f)
        edges.add(f)
        edges.add(t)

    max_l = ""
    for f in edges:
        max_g = find_max_interconnected((f,), edge_map, edges, set())
        if len(max_g) > len(max_l):
            max_l = max_g
            print(max_l, ",".join(max_l))

    return ",".join(max_l)


aoc_day(__file__, solve, "input.txt", "example.txt", "co,de,ka,ta")  # EXAMPLE_MARKER
