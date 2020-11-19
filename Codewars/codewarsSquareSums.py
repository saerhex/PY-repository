def square_sums(n):
    base_list = list(range(1,n + 1))
    seq_list = [square_finder(base_list)]
    backup_list,counter = [],0
    while len(seq_list) < n:
        proper_elements_finding(seq_list,seq_list[-1])
                
    return seq_list

def square_finder(list):
    for num in reversed(list):
        if num ** .5 - int(num ** .5) == 0:
            return list.pop(list.index(num))

def backtracking():
    pass

def proper_elements_finding(list, cons_list_element):
    proper_nums=[]
    for num in list:
        if (num + cons_list_element) ** .5 - int((num + cons_list_element) ** .5) == 0:
            proper_nums.append(num)
    return proper_nums
    

print(square_sums(15))