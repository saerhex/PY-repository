def in_array(array1, array2):
    result = []
    for a1 in array1:
        for a2 in array2:
            if a2.count(a1): 
                result.append(a1)
                break
    return result

a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))