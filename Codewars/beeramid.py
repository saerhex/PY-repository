def beeramid(bonus, price):
    i, result = 1, 0
    while bonus > 0:
        bonus -= (i ** 2) * price
        if bonus < 0:
            break
        result += 1; i += 1
    return result

print(beeramid(5000, 3))