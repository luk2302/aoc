from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 99999999999999999999

    seeds = [int(x) for x in d[0].split(": ")[1].split(" ")]

    maps = []
    current_map = []
    map_index = 0
    for r in range(3, lc, 1):
        l = d[r]
        if not l:
            maps.append(current_map)
            map_index += 1
            current_map = []
            continue
        if not l[0].isdigit():
            continue

        c = [int(x) for x in l.split(" ")]
        current_map.append(c)
        current_map.sort(key=lambda e: e[1])

    for se in range(0, len(seeds), 2):
        solution = min(solution, map_range([(seeds[se], seeds[se+1])], maps))

    return solution


def map_range(inp, maps):
    if not maps:
        print(inp)
        return min([a[0] for a in inp])

    m = maps[0]
    print(inp, m)

    ranges = []
    for st, ra in inp:
        for d, s, r in m:
            if st < s:
                cr = min(s - st, ra)
                ranges.append((st, cr))  # no mapping
                st += cr
                ra -= cr
                if ra == 0:
                    break
            if s <= st < s + r:
                off = st - s
                ar = (s + r) - st
                cr = min(ar, ra)
                ranges.append((d + off, cr))  # mapping
                ra -= cr
                st += cr
                if ra == 0:
                    break
        if ra > 0:
            ranges.append((st, ra))  # no mapping

    return map_range(ranges, maps[1:])


aoc_day(__file__, solve, "input.txt", "example.txt", 46)  # EXAMPLE_MARKER
