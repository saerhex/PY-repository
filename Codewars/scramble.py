from collections import Counter

def scramble(s1, s2):
    l1 = Counter(s1)
    l2 = Counter(s2)
    return True if sum([v for k, v in l2.items() if l1[k] >= v]) == len(s2) else False

print(scramble('scriptingjava', 'javascript'))