from itertools import combinations

def prod(arr, k):
    if k > len(arr):
        return None
    combs = list(map(get_prod, combinations(arr, k)))
    return min(combs), max(combs)

def get_prod(arr):
    r = 1
    for x in arr:
        r *= x
    return r

print(prod([1, -2, -3, 4, 6, 7], 7))