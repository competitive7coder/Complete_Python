def intersection(arr1, arr2):
    result = []
    temp = 0
    arr1.sort()
    arr2.sort()
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            temp = arr1[i]
            if temp not in result:
                result.append(temp)
            i, j = i+1, j+1
        elif arr1[i] < arr2[j]:
            i+= 1
        else:
                j+= 1
    return result
arr1 = [4,9,5]
arr2 = [9,4,9,8,4]
ans = intersection(arr1, arr2)
print(ans)