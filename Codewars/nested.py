def same_structure_as(orig, other):
    orig_struct = get_structure(orig)
    other_struct = get_structure(other)
    return orig_struct == other_struct

def is_nested(item):
    if isinstance(item, list): return True
    else: return False

def get_structure(arr):
    struct = []
    for e in arr:
        if is_nested(e):
            struct.append(get_structure(e))
        else: struct.append(0)
    return struct

a1 = ['[', ']', 1]
a2 = [1, '[', ']'] 
print(same_structure_as(a1, a2))