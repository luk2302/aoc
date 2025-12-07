import re

def ints(s: str):
    return [int(x) for x in re.split('\D', s) if x]

def rotate(l):  # right
    return list(map(list, zip(*l[::-1])))

def transpose(l):
    return list(map(list, zip(*l)))

def to_str(x):
    return ''.join(k if isinstance(k, str) else to_str(k) for k in x)

def bint(b, d = 1, e = 0):
    return d if b else e

def sign(i: int, zero=0):
    return -1 if i < 0 else (1 if i > 0 else zero)

def green(s):
    return "\033[32m" + str(s) + "\033[0m"

def red(s):
    return "\033[31m" + str(s) + "\033[0m"

def bold(s):
    return "\033[1m" + str(s) + "\033[0m"