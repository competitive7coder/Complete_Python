def rd_2(arr):
    for i in range(len(arr)):
        for j in range(i + 2, len(arr)):
            if arr[j] == arr[j-2]:
                continue
                i+= 1
                j+= 1
            else:
                arr[j-1] = arr[j]
    return i
arr = [1,1,1,2,2,3]
ans = rd_2(arr)
print(ans)