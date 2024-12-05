def ints(s: str, d: str = ','):
    return [int(x.strip(' ').strip(d)) for x in s.split(d) if x]

def rotate(l):  # right
    return list(map(list, zip(*l[::-1])))

def transpose(l):
    return list(map(list, zip(*l)))

def to_str(x):
    return ''.join(k if isinstance(k, str) else to_str(k) for k in x)

def bint(b, d = 1, e = 0):
    return d if b else e