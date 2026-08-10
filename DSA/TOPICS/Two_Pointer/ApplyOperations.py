def applyOperations(nums):
    n = len(nums)

    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    write = 0
    for i in range(n):
        if nums[i] != 0:
            nums[write] = nums[i]
            write += 1

    while write < n:
        nums[write] = 0
        write += 1

    return nums
nums = [1,2,2,1,1,0]
ans = applyOperations(nums)
print(ans)