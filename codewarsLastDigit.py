def last_digit(baseNum,rank):
    return 1 if rank==0 else (baseNum%10)**(rank%4+4)%10

print(last_digit(2**200,2**300))