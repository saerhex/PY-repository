def rgb(r, g, b):
    color = [validate(c) for c in [r, g, b]]
    hexed_color = [hex(c).replace('0x','').upper() for c in color]
    return ''.join(near_zero_validate(c) for c in hexed_color)

def validate(component):
    if component < 0:
        return 0
    elif component > 255:
        return 255
    else:
        return component

def near_zero_validate(component):
    if len(component) == 1:
        return '0' + str(component)
    else:
        return component

print(rgb(0,1,2))