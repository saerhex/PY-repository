import re
NAMES = {
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,
        'eleven':11,
        'twelve':12,
        'thirteen':13,
        'fourteen':14,
        'fifteen':15,
        'sixteen':16,
        'seventeen':17,
        'eighteen':18,
        'nineteen':19,
        'twenty':20,
        'thirty':30,
        'fourty':40,
        'fifty':50,
        'sixty':60,
        'seventy':70,
        'eighty':80,
        'ninety':90,
        }

def parse_int(string):
    words = re.split(r'[\s-]{1,}', string)
    words = list(filter(lambda w: w != 'and', words))
    result, temp_sum = 0, 0
    for word in words:
        if word == 'thousand':
            temp_sum *= 1000
            result += temp_sum
            temp_sum = 0
        elif word == 'hundred':
            temp_sum *= 100
        elif word == 'million':
            temp_sum *= 1000000
        else:
            temp_sum += get_number_from(word)
    result += temp_sum
    return result

def get_number_from(name):
    return NAMES[name]

print(parse_int("one"))