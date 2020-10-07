def square_sums(n):
    base_list = list(range(1,n + 1))
    seq_list = [square_finder(base_list)]
    back_list,backup=[[],[]]
    copy_of_list=base_list.copy()
    backtracking(copy_of_list,seq_list[0],back_list,backup)
    seq_list.extend(back_list)
    return seq_list

def square_finder(list):
    for num in reversed(list):
        if num ** .5 - int(num ** .5) == 0:
            return list.pop(list.index(num))

def backtracking(copy_list,cons_list_element,add_list,backup_list):
    proper_list=proper_elements_finding(copy_list, cons_list_element)
    if len(proper_list) == 1:
        add_list.append(copy_list.pop(copy_list.index(proper_list[0])))
        backtracking(copy_list,add_list[-1],add_list,backup_list)
    elif len(proper_list) == 0:
        return None
    else:
        iter_list=iter(proper_list)
        add_list.append(copy_list.pop(copy_list.index(next(iter_list))))
        if backtracking(copy_list,add_list[-1],add_list,backup_list) == None:
            add_list.remove(add_list[-1])
            copy_list=backup_list.copy()
            backtracking(copy_list,next(iter_list),add_list,backup_list)

def proper_elements_finding(list, cons_list_element):
    proper_nums=[]
    for num in list:
        if (num + cons_list_element) ** .5 - int((num + cons_list_element) ** .5) == 0:
            proper_nums.append(num)
    return proper_nums
    

print(square_sums(15))