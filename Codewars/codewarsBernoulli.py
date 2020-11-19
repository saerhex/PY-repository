def bernoulli_number(n):
    _memoized_calculations={0:1}
    _pascal_triangle = [[1, 1]]
    __calculate_and_memoize(1,_memoized_calculations,_pascal_triangle)
    for i in range(2, n + 1):
        __calculate_and_memoize(i,_memoized_calculations,_pascal_triangle)
    return _memoized_calculations[n]

#Calculating binomial coefficients with Pascal's triangle
def __binomial_coefficients_calculate(n,_pascal_triangle):
    binomial_coefficients = [1]
    for i in range(0, n, 1):
        binomial_coefficients.append(_pascal_triangle[0][i] + _pascal_triangle[0][i+1])
    binomial_coefficients.append(1)
    return binomial_coefficients

#Memoizing calculations to re-use them in tne next iteration
def __calculate_and_memoize(n,_memoization_list,_pascal_triangle):
    from fractions import Fraction
    if n % 2 == 0 or n == 1:
        __append_coefficients(n,_pascal_triangle)
        pascal_triangle_sliced = _pascal_triangle[0][:-1]
        numerator = pascal_triangle_sliced[0]
        numerator += sum([_memoization_list[j] * pascal_triangle_sliced[j] for j in range(1,n)])
        denominator = pascal_triangle_sliced[-1]
        result = Fraction(-1 * numerator, denominator)
        _memoization_list[n] = result
    else:
        __append_coefficients(n,_pascal_triangle)
        _memoization_list[n] = 0

def __append_coefficients(n, _pascal_triangle):
    _pascal_triangle.append(__binomial_coefficients_calculate(n,_pascal_triangle))
    _pascal_triangle.pop(0)