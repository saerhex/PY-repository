def solution(args):
    _length = len(args)-1
    filtred_list,temporar_list = [],[]
    range_finding(args,temporar_list,filtred_list,_length)
    result_stroke = ','.join(list(map(str,filtred_list)))
    return result_stroke

def range_finding(base_list,temp_list,filtred_list,length):
    index,control_value,counter = 0,2,0
    while index <= length:
        if control_value == 0:
            counter = 0
            control_value = 2
            index += 1
            filtred_list.append(range_compress_with_separator(temp_list))
            temp_list.clear()
            continue
        if not(base_list[index] in temp_list):
            temp_list.append(base_list[index])
        if index < length - 1:
            temp_list.append(base_list[index+control_value])
        elif index >= length - 1 and index != length:
            temp_list.append(base_list[index+1])
            control_value -= 1
        elif index == length:
            temp_list.append(base_list[index])
            control_value -=1
        if control_value == 2:
            if temp_list[-1]-temp_list[counter] == control_value:
                index += control_value
                counter += 1
            else:
                control_value -= 1
                temp_list.pop()
            continue
        elif control_value == 1:
            if temp_list[-1]-temp_list[counter] == control_value:
                control_value -= 1
                index += 1
            else:
                control_value -= 1
                temp_list.pop()
            continue
        index += 1

def range_compress_with_separator(temp_list):
    if abs(temp_list[-1]-temp_list[0]) >= 2 and len(temp_list) >= 2:
        return str(temp_list[0]) + '-' + str(temp_list[-1]) 
    elif abs(temp_list[-1]-temp_list[0]) == 1 and len(temp_list) >= 2:
        return str(temp_list[0]) + ',' + str(temp_list[-1])
    else:
        return str(temp_list[0])

print(solution([-3,-2,-1,2,10,15,16,18,19,20]))