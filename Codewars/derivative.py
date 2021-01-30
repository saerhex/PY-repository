import re

def differentiate(expression, x):
    content = re.findall(r'-*\d*x\^*\d*', expression)
    differentiated = []
    for item in content:
        coef, power = get_nums(item)
        differentiated.append(get_derivative(coef, power, x))
    return sum(differentiated)
        
regexes = [r'.*(?=x)', r'(?<=\^).*']

def get_nums(string):
    if '^' not in string: power = 1
    else: power = re.search(regexes[1], string).group()
    coef = re.search(regexes[0], string).group()
    if not coef: coef = 1
    if coef == '-': coef = -1
    return int(coef), int(power)

get_derivative = lambda coef, power, x: (coef * power) * x ** (power - 1)

print(differentiate('12x+2', 3))