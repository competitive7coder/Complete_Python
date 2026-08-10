def isPossible(arr, mid, n, k):

    count_painters = 1
    board_sum = 0

    for board in arr:

        if board_sum + board > mid:

            count_painters += 1
            board_sum = board

        else:

            board_sum += board

    return count_painters <= k


def paintersPartition(arr, k):

    n = len(arr)

    if k > n:
        return max(arr)

    start = max(arr) # min possible ans = largest element
    end = sum(arr)

    ans = -1

    while start <= end:

        mid = start + (end - start) // 2

        if isPossible(arr, mid, n, k):

            ans = mid
            end = mid - 1

        else:

            start = mid + 1

    return ans


arr = [5,5,5,5]
k = 2

print(paintersPartition(arr, k))