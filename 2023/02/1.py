from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0

    b = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for r in range(0, lc, 1):
        l = d[r]
        impossible = False
        game, content = l.split(": ")
        game = int(game.split(" ")[1])

        rounds = content.split("; ")
        for round in rounds:
            balls = round.split(", ")
            for ball in balls:
                count, color = ball.split(" ")
                if b[color] < int(count):
                    impossible = True

        if not impossible:
            solution = solution + game

    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 8)  # EXAMPLE_MARKER
