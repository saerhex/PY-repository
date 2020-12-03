def encode(s):
    codes = [ord(c) for c in s]
    bits = [format(c, '08b') for c in codes]
    triples = [d * 3 for bit in bits for d in bit]
    return ''.join(triples)

def decode(bits):
    triples = [bits[i:i+3] for i in range(0, len(bits), 3)]
    bits = [['0', '1'][t.count('0') < t.count('1')] for t in triples]
    codes = [int(''.join(bits[i:i+8]), 2) for i in range(0, len(bits), 8)]
    return ''.join(chr(code) for code in codes)
    
print(decode("000111000111000111000010000000111111000000111111000111111111000000111111000111111111000111010000"))