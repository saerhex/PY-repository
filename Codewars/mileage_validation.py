import string
SUFFIX = ('998', '999')

def is_interesting(number, awesome_phrases):
    if number < 100: return 0
    should_be_mentioned = awesome_phrases +\
                          get_interesting_numbers(number)
    valid = []
    for sh_num in should_be_mentioned:
        if sh_num == number:
            return 2
        if abs(sh_num - number) <= 2:
            valid.append(sh_num)
    if valid:
        return 1
    return 0
            

def get_interesting_numbers(number):
    str_n = str(number)
    len_n = len(str_n)
    nums = [
        trailing_zeros(str_n),
        one_digit(str_n),
        *incr_sequence(len_n),
        *decr_sequence(len_n),
        palindrome(str_n),
    ]
    return nums

#Number followed by trailing zeros   
def trailing_zeros(n: str):
    if n.endswith(SUFFIX):
        w_begin = str(int(n[0]) + 1)
    else: 
        w_begin = n[0]
    return int(w_begin + '0'*(len(n) - 1))

#One digit repeated all the way
def one_digit(n: str):
    return int(n[0] * len(n))

#Sequential part
def decr_sequence(length):
    decr = string.digits[::-1]
    seq_decr = get_sequential(length, decr)
    return list(map(int, seq_decr))
    
def incr_sequence(length):
    incr = string.digits[1:] + '0'
    seq_incr = get_sequential(length, incr)
    return list(map(int, seq_incr))
    
def get_sequential(length, source):
    return [source[i:i + length] for i in range(11 - length)]
    
#Palindrome part
def palindrome(n: str):
    length = len(n)
    b = length // 2
    sep = ''
    if length & 1:
        sep = n[b]
    return int(make_palindrom(n[:b], sep))

def make_palindrom(half, sep):
    return half + sep + half[::-1]

print(is_interesting(67890
, []))