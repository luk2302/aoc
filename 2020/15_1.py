from time import time

start_time = time()
with open("15_input.txt") as f:
    line = f.readline()

numbers = [int(i) for i in line.split(",")]
spoken = {number: index + 1 for index, number in enumerate(numbers)}

last_spoken = numbers[-1]
first = True
turn = len(numbers)

target = 30000000  # 2020
while True:
    turn = turn + 1

    if first:
        speak = 0
    else:
        speak = turn - 1 - spoken[last_spoken]

    if turn % (int(target / 100)) == 0:
        print(f"turn {turn} speaking {speak} - {int(turn / target * 100)}%")
    spoken[last_spoken] = turn - 1
    last_spoken = speak
    first = last_spoken not in spoken

    if turn == target:
        print(f"turn {turn} speaking {speak}")
        break

end_time = time()
print((end_time - start_time))
