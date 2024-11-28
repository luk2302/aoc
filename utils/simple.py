def ints(s: str, d: str = ','):
    return [int(x) for x in s.split(d)]

def rotate(d):  # right
    return list(map(list, zip(*d[::-1])))

def transpose(x):
    return list(map(list, zip(*x)))