from functools import reduce

def greatest_product(n):
    product = []
    for i in range(len(n)-4):
        nums = list(n[i:i+5])
        product.append(reduce(lambda x, y: int(x) * int(y),nums))
    return max(product)

print(greatest_product("02494037820244202221011110532909999"))