def capital():
    n = 1.5 * 10 ** 9
    dep = 100 * 10 ** 3
    n -= dep - dep * 0.10
    while n > 0:
        dep *= 2
        temp = n
        n -= dep
        n += dep * 0.10
    return temp

print(capital())