from collections import Counter
import re

def mix(s1, s2):
    s1, s2 = clear(s1), clear(s2)
    c1, c2 = (Counter(s) for s in (s1, s2))
    letters = {k: v for k, v in (c1 | c2).items() if v != 1}
    vals, res = [], []
    for l, v in letters.items():
        if c1[l] > c2[l]: vals.append('1:' + l * v)
        elif c1[l] < c2[l]: vals.append('2:' + l * v)
        else: vals.append('=:' + l * v)
    min_l, max_l = min_len(vals), max_len(vals) + 1
    for i in range(min_l, max_l):
        res.extend(get_sorted(vals, i))
    return '/'.join(res[::-1])

def clear(s):
    return re.sub(r'[\\/&!?\.\(\) ]', '', s)

def min_len(iterable):
    return len(min(iterable, key=len))

def max_len(iterable):
    return len(max(iterable, key=len))

def get_sorted(iterable, length):
    res = list(filter(lambda e: len(e) == length, iterable))
    return sorted(res, key=lambda x: (x[0], x[2]), reverse=True)


s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
r = "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
print(mix(s1, s2) == r)