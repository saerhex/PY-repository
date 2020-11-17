import re

def leaderboard_sort(leaderboard, changes):
    for change in changes:
        person = (re.findall(r'\w*\s',change)[0]).rstrip()
        action = re.findall(r'[+-]\d*',change)[0]
        index = leaderboard.index(person)
        offset = int(action[1:])
        if action[0] == '+':
            leaderboard.insert(index - offset,leaderboard.pop(index))
        elif action[0] == '-':
            leaderboard.insert(index + offset,leaderboard.pop(index))
    return leaderboard

print(leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1']))