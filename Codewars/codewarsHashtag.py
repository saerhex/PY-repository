def generate_hashtag(s):
    words = [word.title() for word in s.split()]
    hashtag = '#' + ''.join(words)
    return hashtag if len(hashtag) < 140 and s else False

print(generate_hashtag(''))