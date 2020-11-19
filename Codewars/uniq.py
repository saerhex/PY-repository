def uniq(seq):
    result = []
    while seq:
        letter, count = seq[0], 1
        seq.remove(letter)
        count += find_duplicates(seq, letter)
        result.append((letter, count))
    return result

def find_duplicates(array, letter):
    dups_count = 0
    for sym in array[:]:
        if sym == letter:
            array.remove(sym)
            dups_count += 1
        else:
            break
    return dups_count
    
tests = [
    (uniq(['a','a','b','b','c','a','b','c']), [('a',2),('b',2),('c',1),('a',1),('b',1),('c',1)]),
    (uniq(['a','a','a','b','b','b','c','c','c']), [('a',3),('b',3),('c',3)]),
    (uniq([None,'a','a']), [(None, 1),('a', 2)]),
    (uniq(['foo']), [('foo', 1)]),
    (uniq(['']), [('', 1)]),
    (uniq([]), [])
]

for test in tests:
    print(test[0] == test[1])