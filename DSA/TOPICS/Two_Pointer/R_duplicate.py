def remove_duplicate(nums):
    i = 0
    for j in range(i + 1, len(arr)):
        if arr[j] != arr[i]:
            i+= 1
            arr[i] = arr[j]
    return i + 1


arr  = [1,1,1,1,2,2,3,3,3,3,3,4,5,5,6]
ans = remove_duplicate(arr)
print(f"Numbers of duplicate element is: {ans}")