def namelist(names):
    if not names: return ''
    f_part = ', '.join(d['name'] for d in names[:-1])
    s_part = names[-1]['name']
    if not f_part: return s_part
    return ' & '.join((f_part, s_part))

s = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
print(namelist(s))