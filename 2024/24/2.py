import operator
from utils.aoc import *

def num(wires, k):
    zs = [key for key in wires.keys() if key.startswith(k)]
    return int("".join([str(wires[z]) for z in reversed(sorted(zs))]), 2)



def solve(d: str):
    wires, gates = d.split("\n\n")
    wires = {wire.split(": ")[0]: int(wire.split(": ")[1]) for wire in wires.split("\n")}
    gates = gates.split("\n")
    parsed_gates = []
    for gate in gates:
        parts = gate.split(" ")
        op = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}[parts[1]]
        gate = (parts[0], parts[2], op, parts[4])
        parsed_gates.append(gate)

    x = num(wires, "x")
    y = num(wires, "y")
    print("x", bin(x))
    print("y", bin(y))
    print("x+y", bin(x + y))

    changed = True
    while changed:
        changed = False
        for (a, b, op, res) in parsed_gates:
            if a in wires and b in wires and res not in wires:
                wires[res] = op(wires[a],wires[b])
                changed = True
    z = num(wires, "z")
    print("z  ", bin(z))
    print()
    zs = sorted([key for key in wires.keys() if key.startswith("z")])
    previous_influenced = set()
    for z in zs:
        to_check = [z]
        influenced = set()
        xs = set()
        ys = set()
        while to_check:
            check = to_check.pop()
            gate = next(gate for gate in parsed_gates if gate[3] == check)
            for i in (gate[0], gate[1]):
                if i.startswith("x"):
                    xs.add(i)
                elif i.startswith("y"):
                    ys.add(i)
                else:
                    influenced.add(i)
                    to_check.append(i)
        index = int(z[1:])
        valid_result = wires[z] == int(list(reversed(bin(x + y)))[index])
        possibly_valid = all(f"x{i:02}" in xs and f"y{i:02}" in ys for i in range(index + 1))
        print(z, xs, ys, influenced, influenced - previous_influenced)
        if not valid_result:
            # set a breakpoint here and figure out which wires need to be swapped
            #
            # notes from my input
            # first invalid
            # y09 XOR x09 -> wpr
            # switch
            # y09 AND x09 -> z09
            # jnn XOR wpr -> rkf
            #
            #
            # qkq AND stj -> z20
            #
            # CORRECT WIRING IS e.g.
            # Z19 = csn XOR jqw = (x19 XOR y19) XOR (rbc OR kgg) = (x19 XOR y19) XOR ((pfb AND hrn) OR (x18 AND y18))
            #
            # csn XOR jqw -> z19
            # x19 XOR y19 -> csn
            # rbc OR kgg -> jqw
            # x18 AND y18 -> kgg
            # pfb AND hrn -> rbc
            #
            #
            # second invalid
            # qkq AND stj -> z20
            # y20 XOR x20 -> qkq
            # y19 AND x19 -> dwn
            # dwn OR skp -> stj
            # csn AND jqw -> skp
            #
            # stj XOR qkq -> jgb
            #
            #
            # third invalid
            # jnh OR njq -> z24
            # y24 XOR x24 -> tnm
            # hrk AND smg -> vvb
            # knh OR vvb -> kkp
            # x23 AND y23 -> knh
            # kkp AND tnm -> jnh
            # y24 AND x24 -> njq
            #
            # tnm XOR kkp -> vcg
            #
            #
            # fourth invalid
            # csf XOR rrs -> z31
            # fmw AND ffk -> twt
            # x31 AND y31 -> rrs
            # fqm OR twt -> csf
            # x30 AND y30 -> fqm
            #
            # x31 XOR y31 -> rvc
            #
            # switch z09 and rkf, z20 and jgb, z24 and vcg, rvc and rrs
            print(valid_result, possibly_valid)
            pass
        previous_influenced = influenced

    return -1


aoc_day(__file__, solve, "input_fixed.txt", "example2.txt", -1, "FULL")  # EXAMPLE_MARKER
