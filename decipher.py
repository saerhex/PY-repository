import re

def decipher_this(s):
    words, i = s.split(' '), 0
    for word in words:
        letter = re.search(r'\b\d*', word).group(0)
        word = word.replace(letter, chr(int(letter)))
        if len(word) > 2:
            word = ''.join([word[0], word[-1], word [2:-1], word[1]])
        words[i] = word; i += 1
    return ' '.join(words)
    
print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"))