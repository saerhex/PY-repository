import re

def solution(s, markers):
    if markers:
        mark_re = '[' + ''.join('\\' + mark for mark in markers) + ']'
    else:
        return s
    splited, result = s.split('\n'), []
    pattern = fr'(?m:\s*{mark_re}.*?$)'
    for st in splited:
        result.append(re.sub(pattern, '', st))
    return '\n'.join(result)

print(solution("cherries bananas strawberries cherries\napples '\napples apples lemons strawberries ? ?", []))