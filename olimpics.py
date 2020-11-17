st = input().split()
n, k = int(st[0]), int(st[1])
nums, result, cur_limit = [], [] , k
for i in range(n):
    nums.append(int(input()))
j = -1
while nums:
    num = nums[j]
    if len(nums) > 1 and nums[-2] == num:
        cur_limit = num
        count = 0
        while nums:
            if nums[j] != num:
                break
            result.append(cur_limit)
            cur_limit -= 1
            nums.pop()
            count += 1
        continue
    if num > cur_limit:
        result.append(cur_limit)
        cur_limit -= 1
        nums.pop()
    else:
        result.append(num)
        cur_limit = k
        nums.pop()
print('\n')
for res in reversed(result):
    print(res)