def square_sums(n):
    array = list(range(1,n + 1))
    seq_array = [square_finder(array)]
    back_list=[]
    backtracking(array,seq_array,back_list)
    return seq_array

def square_finder(array):
    for num in reversed(array):
        if num ** .5 - int(num ** .5) == 0:
            return array.pop(array.index(num))

def backtracking(base_array,cons_array_element,add_list):
    proper_array=proper_elements_finding(base_array, cons_array_element)
    if proper_array.count() == 1:
        add_list.append()
    elif proper_array.count() == 0:
        return None
    else:
        for i in proper_array:
            backtracking(base_array,add_list[-1],add_list)

def proper_elements_finding(base_array, cons_array_element):
    proper_nums=[]
    for num in base_array:
        if (num + cons_array_element) ** .5 - int((num + cons_array_element) ** .5) == 0:
            proper_nums.append(num)
    return proper_nums
    

print(square_sums(15))