powers = list(range(-24, -2, 3)) + list(range(-2, 3, 1)) + list(range(3, 25, 3))
bases = [10 ** i for i in powers]
prefixes = (['Ym', 'Zm', 'Em', 'Pm', 'Tm',
            'Gm', 'Mm', 'km', 'hm', 'dam',
            'm', 'dm', 'cm', 'mm', 'µm',
            'nm', 'pm', 'fm', 'am', 'zm', 'ym',])[::-1]
metrics = {prefixes[i]: bases[i] for i in range(len(bases))}

def meters(x):
    ans = ''
    for i, v in metrics.items():
        num = x / v
        if num < 1: break
        if num.is_integer(): num = int(num)
        ans = str(num) + i
    return ans

print(meters(12300000))