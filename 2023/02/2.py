from utils.aoc import aoc_day


def solve(d: list[str]):
    lc = len(d)
    w = len(d[0])
    solution = 0


    for r in range(0, lc, 1):
        b = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        l = d[r]
        game, content = l.split(": ")
        game = int(game.split(" ")[1])

        rounds = content.split("; ")
        for round in rounds:
            balls = round.split(", ")
            for ball in balls:
                count, color = ball.split(" ")

                b[color] = max(b[color], int(count))

        solution = solution + b["blue"] * b["green"] * b["red"]


    return solution


aoc_day(__file__, solve, "input.txt", "example.txt", 2286)  # EXAMPLE_MARKER
