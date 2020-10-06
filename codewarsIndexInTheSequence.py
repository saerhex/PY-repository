from itertools import permutations

def next_bigger(n):
    nsArray=list(map(str,str(n)))
    allCombs=list(permutations(nsArray,r=len(nsArray)))
    for i in range(0,len(allCombs)):
        allCombs[i]=''.join(map(str,allCombs[i]))
    nsArray=sorted(set(allCombs))
    return int(nsArray[nsArray.index(str(n))+1])

print(next_bigger(198762534649732664))