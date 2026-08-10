# Basic Syntax
arr = [10, 20, 30, 40]
for i in range(len(arr)):
    print(arr[i])
# len(arr) → total number of elements
# range(len(arr)) → generates indexes 0 to len(arr) - 1
# arr[i] → element at index i


arr = [10, 20, 30, 40]
for i in arr:
    print(i)
#boths returns: 10,20,30,40


# Example 1: Print Elements with Index
arr = [10, 20, 30, 40]
for i in range(len(arr)):
    print("Index:", i, "Value:", arr[i])

# Output
# Index: 0 Value: 10
# Index: 1 Value: 20
# Index: 2 Value: 30
# Index: 3 Value: 40


# Example 2: Modify Each Element
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr[i] = arr[i] * 2

print(arr)
# Output
# [2, 4, 6, 8]

# # You cannot do this with:
# for x in arr:
#     x = x * 2   # ❌ does NOT change the list



# Example 3: Compare Adjacent Elements
arr = [3, 5, 2, 8]
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        print(arr[i], "is greater than", arr[i + 1])

# This pattern is used in:
# sorting
# checking order
# pair problems



# Example 4: Two-Pointer Style (Index Control)
arr = [1, 2, 3, 4, 5]
l = 0
r = len(arr) - 1

while l < r:
    print(arr[l], arr[r])
    l += 1
    r -= 1
#OP: 1 5
   # 2 4

# Used in:
# reversing arrays
# palindrome checks


# Common Mistake (Very Important)
# for i in range(len(arr) + 1):  # ❌
#     print(arr[i])              # IndexError
# # IndexError: list index out of range
# # Correct:
# range(len(arr))  # last index is len(arr) - 1



# Shortcut (When Index + Value Both Needed)
for i, val in enumerate(arr):
    print(i, val)

# But for DSA practice, still prefer:
arr = [10, 20, 30, 40]
for i in range(len(arr)):
    print("Index is:", i , "Element is: ", arr[i])

nums = [10,20,30]
sum = 0
for num in range(len(nums)):
    sum+= nums[num]
print(f"Total sum is:{sum}")


def get_numbers():
    mylist = []

    while True:
        ip = int(input("Enter your numbers: "))

        if ip == 10:
            return mylist, len(mylist)

        mylist.append(ip)

numbers, index = get_numbers()

print("List:", numbers)
print("Index:", index)


