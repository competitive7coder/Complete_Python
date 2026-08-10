def isPossible(arr, mid, k):

    need_subarrays = 1
    subarrays_sum = 0

    for num in arr:

        if subarrays_sum + num > mid:

            need_subarrays += 1
            subarrays_sum = num

        else:

            subarrays_sum += num

    return need_subarrays <= k


def splitArray(arr, k):

    start = max(arr) # min possible ans = largest element
    end = sum(arr)

    while start <= end:

        mid = start + (end - start) // 2

        if isPossible(arr, mid, k):
            end = mid - 1
        else:
            start = mid + 1

    return start


#
arr = [7, 2, 5, 10, 8]
k = 2

#
print(splitArray(arr, k))