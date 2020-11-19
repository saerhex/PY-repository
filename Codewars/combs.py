# from itertools import combinations_with_replacement

# def find(arr, num):
#     combinations = []
#     combs_with_repl = [list(combinations_with_replacement(arr, r)) for r in range(1, len(arr) + 1)]
#     for combination in combs_with_repl:
#         combinations.extend(combination)
#     return len(list(filter(lambda s: sum(s) == num, combinations)))

# print(find([3, 6, 9, 12], 12))