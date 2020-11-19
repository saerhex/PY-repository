def ann(n):
    ann = [1]
    john = [0]
    for i in range(1, n):
        set_john(i, ann, john)
        ann.append(i - john[ann[i-1]])
    return ann

def john(n):
    ann = [1]
    john = [0]
    for i in range(1, n):
        john.append(i - ann[john[i-1]])
        set_ann(i, ann, john)  
    return john

def set_ann(n, ann, john):
    ann.append(n - john[ann[n-1]])

def set_john(n, ann, john):
    john.append(n - ann[john[n-1]])

def sum_ann(n):
    return sum(ann(n))

def sum_john(n):
    return sum(john(n))

print(john(11))
print(sum_ann(115))