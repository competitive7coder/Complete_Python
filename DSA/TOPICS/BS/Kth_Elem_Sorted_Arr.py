""" NOT OPTIMAL
def kthElement(arr1, arr2, k):
    i = j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1

        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged[k - 1] # kth element is the k-1 element in array cause arr starts from 0
    """
# OPTIMAL NO EXTRA ARRAY
def kthElement(arr1, arr2, k):

    i = j = 0
    count = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            count += 1

            if count == k:
                return arr1[i]

            i += 1

        else:
            count += 1

            if count == k:
                return arr2[j]

            j += 1

    while i < len(arr1):

        count += 1

        if count == k:
            return arr1[i]

        i += 1

    while j < len(arr2):

        count += 1

        if count == k:
            return arr2[j]

        j += 1

arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]
k = 5

print(kthElement(arr1, arr2, 2))