def sort_by_name(arr):
    names, nums_count, result = {}, {}, []
    for num in arr:
        nums_count[num] = arr.count(num)
        names[get_name(num)] = num
    sorted_by_name = dict(sorted(names.items(), key=lambda n: n[0]))
    for value in sorted_by_name.values():
        result.extend([value]*nums_count[value])
    return result

NAMES = {0:'',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30:'thirty',
        40:'forty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety',
        100:'hundred'}

def get_name(num):
    name = ''
    if num == 0:
        return 'z'
    hundreds, rest = num // 100, num % 100
    ones = rest % 10
    twenty = rest - ones
    if hundreds > 0:
        name += ' '.join([NAMES[hundreds],NAMES[100],''])
    if twenty >= 20:
        name += ' '.join([NAMES[twenty],NAMES[ones]])
        return name
    if twenty + ones > 10:
        name += NAMES[rest]
        return name
    else:
        name += NAMES[rest]
    return name

print(get_name(801))
# print(sort_by_name([1, 2, 3, 4]))