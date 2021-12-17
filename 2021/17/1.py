

def aoc(inp):
    print(f"reading and processing {inp}")

    inp = inp[15:]
    x, y = inp.split(", y=")
    x1, x2 = x.split("..")
    y2, y1 = y.split("..")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    hy = 0
    c = 0
    for vxs in range(x2 + 1):
        for vys in range(-500, 500):
            vx = vxs
            vy = vys
            px = 0
            py = 0
            hyt = 0

            while True:
                px += vx
                py += vy
                hyt = max(hyt, py)
                if x1 <= px <= x2 and y1 >= py >= y2:
                    hy = max(hy, hyt)
                    c += 1
                    break
                if py < y2:
                    break
                if vx == 0 and not x1 <= px <= x2:
                    break

                vy -= 1
                vx += 0 if vx == 0 else (1 if vx < 0 else -1)

    print(hy, c)


aoc_day = __file__.split("/")[-2]
print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
print("")
aoc("target area: x=20..30, y=-10..-5")
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("target area: x=111..161, y=-154..-101")
print("")
print("--------------------------------------------------------------------------------------------------")
