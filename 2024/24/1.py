import operator
from utils.aoc import *


def solve(d: str):
    lc = len(d)
    wires, gates = d.split("\n\n")
    wires = {wire.split(": ")[0]: int(wire.split(": ")[1]) for wire in wires.split("\n")}
    gates = gates.split("\n")
    parsed_gates = []
    for gate in gates:
        parts = gate.split(" ")
        op = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}[parts[1]]
        gate = (parts[0], parts[2], op, parts[4])
        parsed_gates.append(gate)

    changed = True
    while changed:
        changed = False
        for (a, b, op, res) in parsed_gates:
            if a in wires and b in wires and res not in wires:
                wires[res] = op(wires[a],wires[b])
                changed = True

    zs = [key for key in wires.keys() if key.startswith("z")]
    res = int("".join([str(wires[z]) for z in reversed(sorted(zs))]), 2)

    return res


aoc_day(__file__, solve, "input.txt", "example.txt", 2024, "FULL")  # EXAMPLE_MARKER
