def sum_of_intervals(intervals):
    ranges = [e for interval in intervals for e in range(interval[0], interval[1])]
    return len(set(ranges))

print(sum_of_intervals([(1, 4), (3, 5),(7,10)]))