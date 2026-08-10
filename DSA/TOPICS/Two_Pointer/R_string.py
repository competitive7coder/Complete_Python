def reverse_string(s):
    arr = list(s)
    l, r = 0, len(arr) - 1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return "".join(arr)

s = input("Enter string: ")
result = reverse_string(s)
print("Reversed string:", result)
