# A list is a collection used to store multiple values in one variable.
# Lists are ordered, mutable, and allow duplicate values.


# Creating a List
numbers = [1, 2, 3, 4]
names = ["Raj", "Amit", "Neha"]
mixed = [1, "hello", 3.5, True]


# Accessing Elements (Indexing)
# Indexes start from 0.
names = ["Raj", "Amit", "Neha"]
print(names[0])    # Raj
print(names[-1])   # Neha
print(names.index("Amit")) # 1th idx

# Modifying a List (Mutable)
names[1] = "Ravi"
print(names)   # ['Raj', 'Ravi', 'Neha']


# Common List Operations
# 1. Add Elements
nums = [1, 2, 3]
nums.append("RAJ")# add at end
print(nums)
nums.insert(1, 10)    # add at index

# 2. Remove Elements
nums.remove(10)   # removes value
nums.pop()        # removes last
nums.pop(0)       # removes by index

# 3. Length of List
print(len(nums))

# Looping Through a List
for n in nums:
    print(n)

# With index:
nums = [10, 20, 30]
for i, n in enumerate(nums):
    print(i, n)
# enumerate() gives you both:
# the index
# the value
# at the same time
# Output
# 0 10
# 1 20
# 2 30
# Why Use enumerate()?
# Without it:
# for i in range(len(nums)):
#     print(i, nums[i])
#
# With it:
# for i, n in enumerate(nums):
#     print(i, n)


names = ["Raj", "Amit", "Neha"]
for name in names:
    print(name)
# output:
# Raj
# Amit
# Neha
names = ["Raj", "Amit", "Neha"]
for name in names:
    print(name[0])
# Output
# R
# A
# N
# Inside the loop:
# name is one string at a time
# "Raj"
# "Amit"
# "Neha"
# name[0] → first character of that string
# So step by step:
# "Raj"[0] → R
# "Amit"[0] → A
# "Neha"[0] → N
# Safe version:
for name in names:
    if name:
        print(name[0])



names = ["Raj", "Amit", "Neha"]
for ch in names[0]:
    print(ch, end=" ")
# Output
# R a j

# Membership with Lists
print(3 in nums)      # True
print(100 not in nums)


# List Slicing
nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4])   # [1, 2, 3]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4]

'''
| Method      | Use                |
| ----------- | ------------------ |
| `append()`  | add one item       |
| `extend()`  | add multiple items |
| `insert()`  | add at index       |
| `remove()`  | remove value       |
| `pop()`     | remove by index    |
| `sort()`    | sort list          |
| `reverse()` | reverse list       |
| `count()`   | count occurrences  |
'''

# Sorting a List
nums = [3, 1, 4, 2]
nums.sort()
print(nums)   # [1, 2, 3, 4]


# Reverse sort:

nums.sort(reverse=True)

# Copying Lists (Important!)
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]

# Common Beginner Mistake
b = a   # ❌ same reference

# List Comprehension (Short & Powerful)
squares = [x*x for x in range(5)]
print(squares)


# Key Points to Remember
# Lists are mutable
# Index starts at 0
# Use .append() to add
# Use .copy() to avoid bugs

