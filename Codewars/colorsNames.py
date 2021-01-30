from functools import reduce

def string_color(name):
    if len(name) < 2: return None
    codes = [ord(sym) for sym in name]
    components = [
        sum(codes),
        reduce(__import__('operator').mul, codes),
        codes[0] - sum(codes[1:])
    ]
    return ''.join(convert(comp) for comp in components)

def convert(code):
    return format(abs(code) % 256, '02X')

print(string_color('Jack'))