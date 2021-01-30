def valid_ISBN10(isbn): 
    if not check(isbn): 
        return False
    i = iter(range(1,11))
    code = [get_num(s)*next(i) for s in isbn]
    if sum(code) % 11 == 0:
        return True
    else:
        return False

def get_num(sym):
    if sym == 'X': sym = '10'
    return int(sym)

def check(isbn):
    import re
    if len(isbn) != 10:
        return False
    m = re.match(r'[A-Z]', isbn)
    if m:
        if m.start() != 9:
            return False
        if m.group() != 'X':
            return False
    return True


vars = [
    ('1112223339',True),
    ('048665088X',True),
    ('1293000000',True),
    ('1234554321',True),
    ('1234512345',False),
    ('1293',False),
    ('X123456788',False),
    ('ABCDEFGHIJ',False),
    ('XXXXXXXXXX',False),
]
for var in vars:
    print(valid_ISBN10(var[0]) == var[1])