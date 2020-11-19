import math

def who_is_next(names,r):
    if r < 0:
        return None
    LENGTH = len(names)
    if r < LENGTH:
        RATE_OF_2 = 0
    elif r > LENGTH and r < 10:
        RATE_OF_2 = 1
    else:
        RATE_OF_2 = int(math.log(r // LENGTH + 1,2))
    COUNT_OF_NAMES = LENGTH * (2 ** RATE_OF_2)
    INDEX_OF_LEFT_BORDER = LENGTH * (2 ** RATE_OF_2 - 1)
    SEGMENT_LENGTH = COUNT_OF_NAMES // LENGTH
    result_index = int((r - INDEX_OF_LEFT_BORDER) / SEGMENT_LENGTH)
    return names[result_index] if r > LENGTH else names[result_index - 1]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(who_is_next(names,52))