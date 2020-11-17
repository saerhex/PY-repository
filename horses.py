# def counting_horses(sound_str):
#     i = 0; legs_count = []
#     while i < len(sound_str):
#         if sound_str.count('0') == len(sound_str):
#             break
#         if sound_str[i] != '0':
#             sound_str = change_sound(i, sound_str)
#             legs_count.append(i + 1)
#             i = 0
#             continue
#         i += 1
#     return legs_count

# def get_thumps_pattern(thump_index, sound):
#     repeats = (len(sound) // (thump_index + 1)) + 1
#     pattern = (('0' * thump_index) + '1') * repeats
#     return pattern

# def change_sound(thump_index, sound):
#     pattern = list(map(int, get_thumps_pattern(thump_index, sound)))
#     sound_list = list(map(int, sound))
#     sound_after_removing = list(map(str,[sound_list[j] - pattern[j] for j in range(len(sound))]))
#     sound = ''.join(sound_after_removing)
#     return sound


# print(counting_horses('0212030212'))





def high(x):
    return max(list(x.split()), key = lambda i: score(i))

LOWERCASE_ALPHABET = {chr(i+96):i for i in range(1,27)}

def score(item):
    return sum([LOWERCASE_ALPHABET[letter] for letter in item])

print(high('what time are we climbing up the volcano'))