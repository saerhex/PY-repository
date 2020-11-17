import re

def trump_detector(trump_speech):
    total_vowels = []
    for vowel in 'aeiou':
        pattern = vowel + "{1,}"
        total_vowels.extend(re.findall(rf'{pattern}', trump_speech, flags = re.IGNORECASE))
    total_vowels_count = len(total_vowels)
    extra_vowels_count = sum([length - 1 for vowels in total_vowels if (length := len(vowels)) > 1])
    trumpness_rate = extra_vowels_count / total_vowels_count
    return int(trumpness_rate) if trumpness_rate % 1 == 0 else round(trumpness_rate, 2)

tests = ["I will build a huge wall",
        "HUUUUUGEEEE WAAAAAALL",
        "MEXICAAAAAAAANS GOOOO HOOOMEEEE",
        "America NUUUUUKEEEE Oooobaaaamaaaaa",
        "listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"
]

for test in tests:
    print(trump_detector(test))