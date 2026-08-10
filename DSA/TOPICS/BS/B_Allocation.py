def isPossible(arr, mid, n, m):
    count_students = 1
    pages_sum = 0

    for pages in arr:

        if pages_sum + pages > mid:
            count_students += 1
            pages_sum = pages

        else:
            pages_sum += pages

    return count_students <= m ### students_needed <= m  ====> 2 <= 2  ====> True
## false when s = 0, e = 100 mid is 50 then count_students(3) <= m


def bookallocation(arr, m):

    n = len(arr)

    start = max(arr) # min possible ans = largest element
    end = sum(arr)

    ans = -1
    if m > n:
        return -1

    while start <= end:

        mid = start + (end - start) // 2

        if isPossible(arr, mid, n, m):

            ans = mid
            end = mid - 1

        else:

            start = mid + 1

    return ans


arr = [10, 20, 30, 40]
m = 2

print(bookallocation(arr, m))