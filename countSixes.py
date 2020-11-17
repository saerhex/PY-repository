def count_sixes(n):
    last_digit = str(n)[-1]
    power = n // 10
    if last_digit in ['0', '1', '2', '3']:
        sixes_count = 3 * power
    elif last_digit in ['4', '5', '6', '7']:
        sixes_count = 3 * power + 1
    elif last_digit in ['8', '9']:
        sixes_count = 3 * power + 2
    return sixes_count

def sixes_row(n):
    import re
    list_x, i = [0, 1], 2
    values = {}
    while i < n + 1:
        calculate_next_x(list_x)
        result = re.search(r'(?<=\.)6*', str(list_x[-1])).group(0)
        if result:
            values[i] = result.count('6')
        i += 1
    return values

def calculate_next_x(array):
    cur_x = (array[-1] + array[-2]) / 2
    memoize(array, cur_x)

def memoize(array, value):
    array.append(value)
    array.pop(-3)

num = 48
print(f"6's count of {num} is {count_sixes(num)}")
print(sixes_row(50))