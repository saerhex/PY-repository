def primeFactors(n):
    cur_index = 2
    integer_part = n
    result = ""
    while integer_part != 1:
        leftover_part = integer_part % cur_index
        rates_count,integer_part = calculate_max_rate(leftover_part, integer_part, cur_index)
        if rates_count > 1:
            result += "(%d**%d)" %(cur_index,rates_count)
        elif rates_count == 1:
            result += "(%d)" %(cur_index)
        cur_index += 1
    return result

def calculate_max_rate(leftover_part, integer_part, cur_index):
    rates_count = 0
    if leftover_part == 0:
        rates_count = 1
        integer_part = integer_part // cur_index
        while leftover_part == 0:
            leftover_part = integer_part % cur_index
            integer_part = integer_part // cur_index if leftover_part == 0 else integer_part
            rates_count += 1 if leftover_part == 0 else 0
    return rates_count,integer_part

print(primeFactors(7775460))