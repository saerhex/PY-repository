def meeting(s):
    friends, result = s.split(';'), []
    friends_names = [list(reversed(name.split(':'))) for name in friends]
    surnames = {name[0] for name in friends_names}
    families = {surname: [name[1] for name in friends_names if name[0] == surname] for surname in surnames}
    for key in sorted(families.keys()):
        result.extend([''.join(['(',key.upper(),',',' ',value.upper(),')']) for value in sorted(families[key])])
    return ''.join(result)

print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))