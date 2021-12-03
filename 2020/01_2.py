from time import time

start = time()
with open("01_input.txt") as f:
    input = f.readlines()

numbers = set()
for number in input:
    numbers.add(int(number))

for number in numbers:
    for other_number in numbers:
        opposite = 2020 - number - other_number
        if opposite in numbers:
            print(opposite * number * other_number)

end = time()
print((end - start))
