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

    print(maps)

    for seed in seeds:
        mapping = seed
        for map in maps:
            for d, s, r in map:
                if s <= mapping < s + r:
                    mapping = d + (mapping - s)
                    break

        solution = min(solution, mapping)

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 35)  # EXAMPLE_MARKER
