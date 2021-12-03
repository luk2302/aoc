from time import time

start = time()
with open("01_input.txt") as input_file:
    input = input_file.readlines()

counter = 0
last = 10000000
for i in input:
    n = int(i)
    if n > last:
        counter = counter + 1
    last = n

print(counter)

end = time()
print((end - start))
