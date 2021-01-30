from collections import Counter

def letter_frequency(text):
    freq = [(k, v) for k, v in Counter(clear(text)).items()]
    return sorted(freq, key=lambda x: (x[1], x[0]))[::-1]

clear = lambda t: __import__('re').sub(' ', '', t).lower()

print(letter_frequency('aaAabb dddDD hhcc'))
