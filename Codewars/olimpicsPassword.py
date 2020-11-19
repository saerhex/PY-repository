import re

N, a, b = tuple(input().split())
for i in range(int(N)):
    st = input()
    if not re.fullmatch(r'[A-Za-z_]*', st):
        print("Incorrect")
        continue
    if not re.fullmatch(r'[^Il]*', st):
        print("Incorrect")
        continue
    if not len(st) == int(a):
        print("Incorrect")
        continue
    if not len(set(st)) == int(b):
        print("Incorrect")
        continue
    if re.findall(r'(.)\1', st):
        print("Incorrect")
        continue
    else:
        print("Correct")