from itertools import cycle

def spiralize(size):
    spiral = [[0 for i in range(0,size)] for j in range(0,size)]
    current_point = [0,0]
    states = [1,2,3,4]
    flag = False
    counter = 0
    for i in cycle(states):
        if i == 1:
            spiral,flag,current_point = fill_right(spiral,current_point,counter)
            counter += 1
        elif i == 2:
            spiral,flag,current_point = fill_down(spiral,current_point,counter)
            counter += 1
        elif i == 3:
            spiral,flag,current_point = fill_left(spiral,current_point,counter)
            counter += 1
        elif i == 4:
            spiral,flag,current_point = fill_up(spiral,current_point,counter)
            counter += 1
        if flag:
            break
    return spiral

def fill_down(array,current_point,lines_count):
    start_column = current_point[1]
    row_index = current_point[0]
    flag = False
    while not flag:
        if row_index < len(array) - 2:
            if array[row_index+2][start_column] == 1:
                if lines_count == len(array):
                    return array,True,None
                else:
                    flag = True
                    array[row_index][start_column] = 1
                    continue
        if row_index == len(array) - 1:
            array[row_index][start_column] = 1
            flag = True
        else:
            array[row_index][start_column] = 1
            row_index += 1
    return array,False,[row_index,start_column]

def fill_up(array,current_point,lines_count):
    start_column = current_point[1]
    row_index = current_point[0]
    flag = False
    while not flag:
        if row_index > 1:
            if array[row_index-2][start_column] == 1:
                if lines_count == len(array):
                    return array,True,None
                else:
                    flag = True
                    array[row_index][start_column] = 1
                    continue
        if row_index == 0:
            array[row_index][start_column] = 1
            flag = True
        else:
            array[row_index][start_column] = 1
            row_index -= 1
    return array,False,[row_index,start_column]

def fill_right(array,current_point,lines_count):
    start_row = current_point[0]
    column_index = current_point[1]
    flag = False
    while not flag:
        if column_index < len(array[0])-2:
            if array[start_row][column_index+2] == 1:
                if lines_count == len(array):
                    return array,True,None
                else:
                    flag = True
                    array[start_row][column_index] = 1
                    continue
        if column_index == len(array[0]) - 1:
            array[start_row][column_index] = 1
            flag = True
        else:
            array[start_row][column_index] = 1
            column_index += 1
    return array,False,[start_row,column_index]

def fill_left(array,current_point,lines_count):
    start_row = current_point[0]
    column_index = current_point[1]
    flag = False
    while not flag:
        if column_index > 1:
            if array[start_row][column_index-2] == 1:
                if lines_count == len(array):
                    return array,True,None
                else:
                    flag = True
                    array[start_row][column_index] = 1
                    continue
        if column_index == 0:
            array[start_row][column_index] = 1
            flag = True
        else:
            array[start_row][column_index] = 1
            column_index -=1
    return array,False,[start_row,column_index]

print(spiralize(10))