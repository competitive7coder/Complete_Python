# def Sq_sorted_array(arr):
#     result = []
#     for i in range(len(arr)): //for x in arr:
#         sq = arr[i] * arr[i] //     result.append(x * x)
#         result.append(sq)
#         result.sort()
#     return result

# arr = [-4, -1, 0, 3, 10]
# ans = Sq_sorted_array(arr)
# print(ans)


def Sq_sorted_array(arr):
    n = len(arr)                 # length of input array
    res = [0] * n                # new array of size n
    l, r = 0, n - 1
    pos = n - 1                  # position to fill in result (from end)

    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            res[pos] = arr[l] * arr[l]
            l += 1
        else:
            res[pos] = arr[r] * arr[r]
            r -= 1
        pos -= 1                 # move to next position

    return res


# Test
arr = [-4, -1, 0, 3, 10]
ans = Sq_sorted_array(arr)
print("your original array: ",arr)
print(F"Squared of Your sorted array: {ans}")


