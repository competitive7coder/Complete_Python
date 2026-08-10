def SAP(nums):
    s, e = 0, len(nums) - 1
    while s < e:
        if nums[s] % 2 == 0:
            s += 1
        elif nums[e] % 2 != 0:
            e -= 1
        else:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
    return nums

nums = [3,1,2,4]
ans = SAP(nums)
print(f"Expeted O/P is: {ans}")