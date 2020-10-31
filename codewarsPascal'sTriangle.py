# def generate_diagonal(n,l):
#     _pascal_triangle = [[1],[1,1]]
#     for i in range(2, l+n):
#         __binomial_coefficients_calculate(i, _pascal_triangle)
#     return [_pascal_triangle[j][n] for j in range(n,l+n)]

def pascals_triangle(n):
    _pascal_triangle = []
    if n >= 1:
        _pascal_triangle.append([1])
    if n >= 2:
        _pascal_triangle.append([1,1])
    if n >= 3:
        for i in range(3, n+1):
            __binomial_coefficients_calculate(i, _pascal_triangle)
    _result = []
    for row in _pascal_triangle:
        for num in row:
            _result.append(num)
    return _result

def __binomial_coefficients_calculate(n,_pascal_triangle):
    binomial_coefficients = [1]
    for i in range(0, n-2):
        binomial_coefficients.append(_pascal_triangle[-1][i] + _pascal_triangle[-1][i+1])
    binomial_coefficients.append(1)
    _pascal_triangle.append(binomial_coefficients)

print(pascals_triangle(5))