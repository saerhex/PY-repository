ALPHABET_S = "abcdefghijklmnopqrstuvwxyz"
from itertools import cycle

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key
        self.vig_square = self.create_square()

    def encode(self, text):
        cipher, encoded_text = iter(self.make_cipher(text)), ""
        for sym in text:
            cipher_sym = next(cipher)
            if sym in self.alphabet:
                encoded_text += self.vig_square[cipher_sym][self.alphabet.index(sym)]
            else:
                encoded_text += sym
        return encoded_text
    
    def decode(self, text):
        cipher, decoded_text = iter(self.make_cipher(text)), ""
        for sym in text:
            cipher_sym = next(cipher)
            if sym in self.alphabet:
                decoded_text += self.alphabet[self.vig_square[cipher_sym].index(sym)]
            else:
                decoded_text += sym
        return decoded_text

    def make_cipher(self, text):
        cipher, key_iter = "", cycle(self.key)
        for sym in text:
            if sym in self.alphabet: 
                cipher += next(key_iter)
            else: 
                cipher += sym
        return cipher

    def create_square(self):
        square, alph = {}, self.alphabet
        for a in alph:
            index = alph.index(a)
            square[a] = alph[index:] + alph[:index]
        return square

c = VigenereCipher('password', ALPHABET_S)
print(c.decode(c.encode("it's a shift cipher!")))
