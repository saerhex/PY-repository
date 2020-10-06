def solve(m):
    discr=(2 * m + 1)**2 - 4 * m**2
    if discr > 0:
        return (2*m + 1 - discr**0.5) / (2*m)

print(solve(8.0))