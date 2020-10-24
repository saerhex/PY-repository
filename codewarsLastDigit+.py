def last_digit(base_list):
    while len(base_list) > 2:
        result_rate = last_two_digits(base_list[-2],base_list[-1])
        base_list.remove(base_list[-2])
        base_list.remove(base_list[-1])
        base_list.append(result_rate)
    return last_digit_result(base_list[-2],base_list[-1]) if base_list else 1
    
def last_two_digits(base_num,rank):
    return 1 if rank==0 else pow(base_num,rank,4)+4

def last_digit_result(base_num,rank):
    return 1 if rank==0 else pow(base_num,rank,10)

print(last_digit([499942, 898102, 846073]))