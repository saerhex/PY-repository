VOWELS = ['a', 'i', 'y', 'e', 'o', 'u']
CONS = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

def tongues(code):
    encoded = ""
    for sym in code:
        if sym.lower() in VOWELS:
            encoded += encode(sym, VOWELS, 3)
        elif sym.lower() in CONS:
            encoded += encode(sym, CONS, 10)
        else:
            encoded += sym
    return encoded

def encode(symbol: "string", state: "VOWEL, CONS", delay):
    encoded = ''
    index = state.index(symbol.lower())
    encoded_sym = state[(index - delay) % len(state)]
    if symbol.isupper():
        encoded = encoded_sym.upper()
    else:
        encoded = encoded_sym
    return encoded

print(tongues('Ita dotf ni dyca nsaw ecc.'))