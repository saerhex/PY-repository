import re

def matches(snippet):
    tags = re.findall(r'<.*?>', snippet)
    while tags:
        tag = tags[0]
        closing_tag = '/'.join([tag[0], tag[1:]])
        if closing_tag in tags:
            tags.remove(closing_tag)
            tags.remove(tag)
        else: return False
    return True

print(matches("<div></divv>"))