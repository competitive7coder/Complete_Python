def move_zeros(arr):
    i = 0
    for j in range(i+1, len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i+= 1
    return arr

arr = [0, 1, 0, 3, 4, 5]
ans = move_zeros(arr)
print(f"Array with end zero: {ans}")