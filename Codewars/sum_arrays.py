def sum_arrays(array1,array2):
    nums = [get_int(array1), get_int(array2)]
    result = [num for num in nums if not num is None]
    return set_list(result)

def get_int(args):
    if args: return int(''.join(map(str, args)))
    else: return None

def set_list(args):
    if args: result = list(str(sum(args)))
    else: return []
    if result[0] == '-': result[0] += result.pop(1)
    return list(map(int, result))

print(sum_arrays([-8, 7, 7, 8, 3], [7, 4]))