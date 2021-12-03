from time import time


class P:
    pass

class S:
    pass

class M:
    pass

class N:
    pass

def evaluate(line):
    line = line.strip("\n").replace(" ", "")
    stack = []
    for c in line:
        if c == "(":
            stack.append(P())
        elif c == ")":
            stack.pop()
        elif c == "+":
            left = stack.pop()
            stack.append(S(left))
        elif c == "*":
            left = stack.pop()
            stack.append(M(left))
        else:
            last = stack[-1]
            if isinstance(last, N):
                last.update(c)




    return 0


def some():
    start_time = time()
    with open("18_input.txt") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        sum = sum + evaluate(line)

    end_time = time()
    print((end_time - start_time))


some()