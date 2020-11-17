import re
import math

def expand(s):
    power = get_power(s)
    if power == 0:
        return "1"
    letter = get_letter(s)
    a_coefficient = get_a_coefficient(s)
    b_coefficient = get_b_coefficient(s)
    if b_coefficient == 0:
        return ''.join([get_right_value(a_coefficient ** power), letter, '^', power])
    binomial_coefficients = [get_binomial_coefficient(power, k) for k in range(power + 1)]
    a_powers = [a_coefficient ** pw for pw in reversed(range(power + 1))]
    b_powers = [b_coefficient ** pw for pw in range(power + 1)]
    experssion_coefficients = list(map(lambda x: get_prod(x), zip(binomial_coefficients, a_powers, b_powers)))
    experssion = create_expression(experssion_coefficients, letter, power)
    return experssion

def get_power(s):
    return int(re.findall(r'(?<=^)?[0-9]{1,}(?=$)', s, re.MULTILINE)[0])

def get_letter(s):
    return re.findall(r'[A-Za-z]', s)[0]

def get_a_coefficient(s):
    search_result = re.search(r'(?<=\().*?(?=[A-Za-z])', s).group(0)
    if search_result:
        if search_result == '-':
            return -1
        else:
            return int(search_result)
    else:
        return 1

def get_b_coefficient(s):
    return int(re.findall(r'(?<=[A-Za-z]).*?(?=\))', s)[0])

def create_expression(coefficients, letter, power):
    expressions = []
    if power == 1:
        expressions = [f"{get_right_value(coefficients[0])}{letter}", f"{coefficients[1]}"]
        if coefficients[1] > 0:
            expressions[1] = '+' + expressions[1] 
        return ''.join(expressions)
    for i in range(power + 1):
        express = f""
        if i == 0:
            express += f"{get_right_value(coefficients[i])}"
        else:
            express += f"{coefficients[i]}"
        if coefficients[i] > 0 and i != 0:
            express = '+' + express
        if (power - i) > 0:
            express += f"{letter}"
        if (power - i) > 1:
            express += f"^{power - i}"
        expressions.append(express)
    return ''.join(expressions)

def get_binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def get_prod(arr):
    product = 1
    for arg in arr:
        product *= arg
    return product

def get_right_value(coefficient):
    if coefficient == 1:
        return ''
    if coefficient == -1:
        return '-'
    else:
        return f'{coefficient}'

tests=[
        # 
        
        (expand("(n+11)^1"), "1"),
]

for test in tests:
    print(f"{test[0] == test[1]}")