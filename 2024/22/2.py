from collections import defaultdict
from utils.aoc import *


def solve(d: list[str]):
    lc = len(d)
    possible_ranges = defaultdict(lambda: 0)
    for r in range(0, lc, 1):
        l = int(d[r])
        bananas = 0
        pcs = tuple()
        seen_pcs = set()
        for i in range(2000):
            l = ((l << 6) ^ l) & 0b111111111111111111111111
            l = ((l >> 5) ^ l) & 0b111111111111111111111111
            l = ((l << 11) ^ l) & 0b111111111111111111111111
            new_bananas = l % 10
            pcs = (*pcs[-3:], new_bananas - bananas)
            if len(pcs) == 4:
                if pcs not in seen_pcs:
                    seen_pcs.add(pcs)
                    possible_ranges[pcs] += new_bananas
            bananas = new_bananas

    max_range = None
    max_price = 0
    for sell_range, price in possible_ranges.items():
        if price > max_price:
            max_price = price
            max_range = sell_range

    print(max_range)
    return max_price


aoc_day(__file__, solve, "input.txt", "example2.txt",  23)  # EXAMPLE_MARKER
