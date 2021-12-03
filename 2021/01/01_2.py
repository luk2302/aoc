from time import time

start = time()
with open("01_input.txt") as input_file:
    input = input_file.readlines()

counter = 0
for i in range(len(input) - 3):
    if int(input[i]) < int(input[i+3]):
        counter = counter + 1

print(counter)

end = time()
print((end - start))
