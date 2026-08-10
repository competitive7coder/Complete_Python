def MTSA(arr1, arr2):
    """
    def median(arr1, arr2):

        arr = arr1 + arr2
        arr.sort()

        n = len(arr)

        if n % 2 == 1:
            return arr[n // 2]

        return (arr[n // 2] + arr[n // 2 - 1]) / 2
        """

    n1, n2 = len(arr1), len(arr2)

    i = j = 0
    merged = []

    while i < n1 and j < n2:

        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1

        else:
            merged.append(arr2[j])
            j += 1

    while i < n1:
        merged.append(arr1[i])
        i += 1

    while j < n2:
        merged.append(arr2[j])
        j += 1

    n = len(merged)

    if n % 2 == 1:
        return merged[n // 2]

    return (merged[n // 2] + merged[(n // 2) - 1]) // 2


arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

print(MTSA(arr1, arr2))