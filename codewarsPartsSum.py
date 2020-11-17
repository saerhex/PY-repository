def parts_sums(ls):
    sums = [sum(ls)]
    for i in ls:
        sums.append(sums[-1] - i)
    return sums