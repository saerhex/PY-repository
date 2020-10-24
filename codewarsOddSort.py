def sort_array(source_array):
    odd_nums = sorted([num for num in source_array if num % 2 == 1])
    index = 0
    while odd_nums:
        if source_array[index] % 2 == 1:
            source_array[index] = odd_nums[0]
            odd_nums.remove(odd_nums[0])
        index += 1
    return source_array

print(sort_array([5, 3, 1, 8, 0]))