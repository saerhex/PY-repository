from timer import timer

def decompose(n):
    result = []
    cur = n**2
    while cur > 0:
        if not result:
            sq = nearest_square(cur, True)
        else:
            sq = nearest_square(cur)
        if not sq: 
            return None
        non_sq = sq**0.5
        if non_sq in result:
            return None
        cur -= sq
        result.append(sq**0.5)
    return result
        
def nearest_square(limit, strict=False):
    answer = 0
    while less_than(answer, limit, strict):
        answer += 1
    return answer**2

def less_than(num, limit, strict):
    if strict:
        return (num + 1)**2 < limit
    else:
        return (num + 1)**2 <= limit

print(decompose(50))