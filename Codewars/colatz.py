def collatz(n):
    if n == 1: return '1'
    res = [str(n)]
    cur = get_collatz(n)
    res.append(str(cur))
    while cur != 1:
        cur = get_collatz(cur)
        res.append(str(cur))
    return '->'.join(res)
    
def get_collatz(n):
    if n & 1: return 3 * n + 1
    else: return n // 2

c = [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
r = '->'.join(map(str, c))
print(collatz(19) == r)