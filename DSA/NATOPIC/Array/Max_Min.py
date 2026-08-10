def find_min_max(arr):
    mn = arr[0]
    mx = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < mn:
            mn = arr[i]
        if arr[i] > mx:
            mx = arr[i]

    return mn, mx
arr = [10, 40, 20, 70, 30]

mn, mx = find_min_max(arr)

print("Min is:", mn)
print("Max is:", mx)