# def two_pointer(target,arr):
#     for i in range(len(arr)):
#         for j in range(1, len(arr)):
#             if target == arr[i] + arr[j]:
#                 ans = target
#                 return ans
# target = 9
# arr = [7,2,11,5]
# ans = two_pointer(target,arr)
# print("Sum of Array is:",  ans)



# def two_pointer(target,arr):
#     ans = 0
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#             if target == arr[left] + arr[right]:
#                 return arr[left], arr[right]
#             elif target > arr[left] + arr[right]:
#                 left += 1
#             else:
#                 right-= 1
#     return None
# target = 9
# arr = [7,2,11,5]
# ans = two_pointer(target,arr)
# print("Sum of Array is:",  ans)



def two_sum(target, arr):
    mp = {}

    for i in range(len(arr)):
        need = target - arr[i]
        if need in mp:
            return [mp[need], i]
        mp[arr[i]] = i

    return None


target = 9
arr = [7, 2, 11, 5]
ans = two_sum(target, arr)
print(ans)



