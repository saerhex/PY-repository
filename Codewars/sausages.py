from collections import Counter

def unpack_sausages(truck):
    sausages = []
    for box in truck:
        sausages.extend(get_sausages_from(box))
    del sausages[4::5]
    return join_sausage(sausages)

def get_sausages_from(box):
    sausages = []
    for pack in box:
        if '[' in pack and len(Counter(pack)) == 3:
            sausages.append(join_sausage(pack[1:-1]))
    return sausages

join_sausage = lambda iterable: ' '.join(iterable)

print(unpack_sausages(
[("(-)", "[IIII]", "[))))]"), ("IuI", "[llll]"), ("[@@@@]", "UwU", "[IlII]"), ("IuI", "[))))]", "x"), ()]))