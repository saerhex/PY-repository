import itertools

def snail(array):
    result, cur_position = [*array[0]], [1,len(array) - 1]
    if len(array[0]) == 0:
        return []
    else:
        cur_length = len(array) - 1
    for c in itertools.cycle([1,2,3,4]):
        if c == 1 or c == 3:
            result.extend(fill_up_down(cur_length,cur_position,array,c))
        elif c == 2 or c == 4:
            result.extend(fill_sideway(cur_length,cur_position,array,c))
            cur_length -= 1
        if len(result) == len(array) ** 2:
            break
    return result

def fill_sideway(length,cur_pos,array,iteration):
    row = array[cur_pos[0]]
    start = cur_pos[1]
    if iteration == 2:
        end = start - length
        sliced = row[start:end:-1] if end >= 0 else row[start::-1]
        cur_pos[0] -= 1 
        cur_pos[1] = end + 1
    else:
        end = start + length
        sliced = row[start:end]
        cur_pos[0] += 1 
        cur_pos[1] = end - 1
    return sliced

def fill_up_down(length,cur_pos,array,iteration):
    column = cur_pos[1]
    start = cur_pos[0]
    if iteration == 1:
        end = start + length
        sliced = [array[i][column]for i in range(start,end)]
        cur_pos[0] = end - 1
        cur_pos[1] -= 1
    else:
        end = start - length
        sliced = [array[i][column]for i in range(start,end,-1)]
        cur_pos[0] = end + 1
        cur_pos[1] += 1
    return sliced

print(snail([[]]))