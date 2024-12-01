def ints(s: str, d: str = ','):
    return [int(x.strip(' ').strip(d)) for x in s.split(d) if x]

def rotate(d):  # right
    return list(map(list, zip(*d[::-1])))

def transpose(x):
    return list(map(list, zip(*x)))

def to_str(x):
    return ''.join(k if isinstance(k, str) else to_str(k) for k in x)