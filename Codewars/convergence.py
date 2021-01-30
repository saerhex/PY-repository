import operator as op
import functools

def convergence(n):
    base_1, base_n = [1], [n]
    while True:
        base_1.append(calc_next_memb(base_1[-1]))
        base_n.append(calc_next_memb(base_n[-1]))
        inter = set(base_1) & set(base_n)
        if inter:
            break
    return base_n.index(inter.pop())

def calc_next_memb(n):
    if n < 10:
        return 2 * n
    else:
        return n + get_product(n)

def get_product(n):
    return functools.reduce(op.mul, get_digits(n))

def get_digits(n):
    return [int(d) for d in str(n) if d != '0']

print(convergence(3))