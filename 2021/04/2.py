import json


def aoc(input_path, expected_solution=None):
    print(f"reading and processing {input_path}")
    with open(input_path) as input_file:
        day_input = input_file.read()  # without line splits


    # solution starts here #


    boards = day_input.split("\n\n")
    print(len(boards))

    numbers = [int(i) for i in boards[0].split(",")]

    boards_int = []
    for board_input in boards[1:]:
        board = []
        for line_input in board_input.split("\n"):
            ints = [(int(i), False) for i in line_input.strip().replace("  ", " ").split(" ")]
            board.append(ints)
        boards_int.append(board)

    solved_board = 0
    solved_boards = set()

    for n in numbers:
        for board in boards_int:
            for line in board:
                for index in range(len(line)):
                    i, h = line[index]
                    if i == n:
                        line[index] = (i, True)

        for index in range(len(boards_int)):
            if index in solved_boards:
                continue
            board = boards_int[index]
            for line in board:
                if all(h for i, h in line):
                    solved_board = board
                    solved_boards.add(index)
            for i in range(len(board[0])):
                if all(row[i][1] for row in board):
                    solved_board = board
                    solved_boards.add(index)
        if len(solved_boards) == len(boards_int):
            break

    sum = 0
    print(solved_board)
    for line in solved_board:
        for index in range(len(line)):
            i, h = line[index]
            if not h:
                sum = sum + i

    print(sum)
    print(n)
    solution = n * sum


    # solution ends here #



    print(f"solution: {solution}")
    if expected_solution:
        if expected_solution != solution:
            print(f"WARNING: solution does not match expected solution of {expected_solution}")
        else:
            print("matches expected solution :)")


aoc_day = __file__.split("/")[-2]
print(f"---------+ Day {aoc_day} example +-----------------------------------------------------------------------")
print("")
expected_solution = 1924
aoc("example.txt", expected_solution)
print("")
print(f"---------+ Day {aoc_day} solution +----------------------------------------------------------------------")
print("")
aoc("input.txt")
print("")
print("--------------------------------------------------------------------------------------------------")
