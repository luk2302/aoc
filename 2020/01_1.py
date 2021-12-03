from time import time

start = time()
with open("01_input.txt") as input_file:
    input = input_file.readlines()

for first in range(0, len(input)):
    for second in range(first + 1, len(input)):
        for third in range(second + 1, len(input)):
            result = int(input[first]) + int(input[second]) + int(input[third])
            if result == 2020:
                print(int(input[first]) * int(input[second]) * int(input[third]))

end = time()
print((end - start))
