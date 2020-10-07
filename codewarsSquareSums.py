def square_sums(n):
    base_list = list(range(1,n + 1))
    seq_list = [square_finder(base_list)]
    back_list,backup=[[],[]]
    backtracking(base_list,seq_list[0],back_list,backup)
    seq_list.extend(back_list)
    return seq_list

def square_finder(list):
    for num in reversed(list):
        if num ** .5 - int(num ** .5) == 0:
            return list.pop(list.index(num))

def backtracking(array,cons_list_element,add_list,backup_list):
    proper_list=proper_elements_finding(array, cons_list_element)
    if len(proper_list) == 1:
        removeable_num = array.pop(array.index(proper_list[0]))
        if backup_list:
            backup_list.append(removeable_num)
        add_list.append(removeable_num)
        backtracking(array,add_list[-1],add_list,backup_list)
    elif len(proper_list) == 0:
        return None
    else:
        iter_list=iter(proper_list)
        removeable_num = array.pop(array.index(next(iter_list)))
        backup_list.clear()
        backup_list.append(removeable_num)
        add_list.append(removeable_num)
        if backtracking(array,add_list[-1],add_list,backup_list) == None:
            array.extend(backup_list)
            add_list=[item for item in add_list if item not in backup_list]
            backup_list.clear()
            add_list.append(array.pop(array.index(next(iter_list))))
            backtracking(array,add_list[-1],add_list,backup_list)

def proper_elements_finding(list, cons_list_element):
    proper_nums=[]
    for num in list:
        if (num + cons_list_element) ** .5 - int((num + cons_list_element) ** .5) == 0:
            proper_nums.append(num)
    return proper_nums
    

print(square_sums(15))