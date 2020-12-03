get_letters = lambda s: set(s.replace(' ',''))

def find_uniq(arr):
    for word in arr:
        letters = get_letters(word)
        i = arr.index(word)
        for item in (arr[:i] + arr[i+1:]):
            if not get_letters(item) & letters: return item

print(find_uniq([ 'foo', 'abc', 'acb', 'bac',  'bca', 'cab', 'cba' ]))