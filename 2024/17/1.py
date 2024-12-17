from functools import cache
from utils.aoc import *
from utils.graph import *
from utils.simple import *


def solve(d: str):
    regs, prog = d.split("\n\n")
    regs = ints(regs)
    prog = ints(prog)
    ip = 0
    out = []
    while ip < len(prog):
        ins = prog[ip]
        ope = prog[ip + 1]
        opev = ope if ope < 4 else regs[ope - 4]
        print(ip, ins, ope, opev, regs)
        # diving A by 8 until we reach 0
        # B = (A mod 8) xor 1
        if ins == 0:
            print("  A = A / 8")
            regs[0] = int(regs[0] / (2 ** opev))
        if ins == 1:
            print("  B = B xor", ope)
            regs[1] = regs[1] ^ ope
        if ins == 2:
            regs[1] = opev % 8
            print("  B = A mod 8")
        if ins == 3:
            if regs[0] != 0:
                print()
                print()
                print("jumping form", ip, ope)
                ip = ope
                continue
        if ins == 4:
            print("  B = B xor C")
            regs[1] = regs[1] ^ regs[2]
        if ins == 5:
            print("  outputting B % 8 = ", str(opev % 8))
            print("  should output", prog[len(out)])
            out.append(str(opev % 8))
        if ins == 6:
            print("  dividing B", opev, ope)
            regs[1] = int(regs[0] / (2 ** opev))
        if ins == 7:
            print("  C = A / 2 ** B")
            regs[2] = int(regs[0] / (2 ** opev))
        ip += 2

    res = ",".join(out)
    print(prog)
    print(res)
    return res


aoc_day(__file__, solve, "input.txt", "example.txt", "4,6,3,5,6,3,5,2,1,0", "FULL")  # EXAMPLE_MARKER
