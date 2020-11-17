import re

def solve(s):
    res = s
    while s:
        repeats = re.search(r'((\d)*|([A-Za-z])*)(?=\([\w\s]*\))', res)
        expression = re.search(r'(?<=(\d|[A-Za-z])\()\w*(?=\))', res)
        if expression and repeats:
            expr = expression.group(0); rep = repeats.group(0)
            replacement = ''.join([rep, '(', expr, ')'])
            if rep.isdigit():
                res = res.replace(replacement, expr * int(rep))
                s = s.replace(replacement, '')
            else:
                res = res.replace(replacement, rep + expr)
                s = s.replace(replacement, '')
        else:
            break
    return res

tests = [
    ("3(ab)", "ababab"),
    ("2(a3(b))","abbbabbb"),
    ("3(b(2(c)))","bccbccbcc"),
    ("k(a3(b(a2(c))))","kabaccbaccbacc"),
]

for test in tests:
    print(solve(test[0]) == test[1])
