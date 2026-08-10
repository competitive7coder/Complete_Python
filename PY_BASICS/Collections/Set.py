# unordered hota hai
# unique elements rakhta hai (duplicates allowed nahi)
# mutable hota hai (add/remove kar sakte ho)
s = {1, 2, 3}
print(s)



# Set me duplicate values automatically remove ho jaati hain
s = {1, 2, 2, 3, 3}
print(s)
# Output:
{1, 2, 3}



s = {}      # ❌ this is DICTIONARY, not set
s = set()   # ✅ empty set
print(type({}))     # dict
print(type(set()))  # set



# ❌ Indexing allowed nahi
s = {10, 20, 30}
# print(s[0])   # ❌ Error
# ✅ Loop se access
for x in s:
    print(x)
# Set unordered hota hai, isliye index ka concept nahi hota.


# Add single element
s = {1, 2}
s.add(3)
print(s)
# OP: {1, 2, 3}


# Add multiple elements
s.update([4, 5, 6])
print(s)
# OP: {1, 2, 3, 4, 5, 6}


# Remove elements
s.remove(3)     # error if not present
s.discard(10)   # no error if not present
print(s)
# OP: {1, 2, 4, 5, 6}


# Difference:
# remove() → error throw karta hai
# discard() → silently ignore karta hai


# Membership check (Set ka biggest power)
s = {1, 2, 3, 4}
print(3 in s)     # True
print(10 in s)    # False
# ⚡ FAST
# Set me in check → O(1)
# List me in check → O(n)


# Common Set Operations (VERY IMPORTANT)
# Union (|)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
# Output:
{1, 2, 3, 4, 5}


# Intersection (&)
print(a & b)
# Output:
{3}


# Difference (-)
print(a - b)
# Output:
{1, 2}


# Symmetric Difference (^)
print(a ^ b)
# Output:
{1, 2, 4, 5}


# Set ka DSA use-case
# 1️⃣ Remove duplicates from list
arr = [1, 2, 2, 3, 3, 4]
unique = list(set(arr))
print(unique)
#set(arr)--removes duplicates
#list({1, 2, 3, 4}) Set ko wapas list me convert kar rahe hain.

# 1️⃣ Remove duplicates from list
# 1️⃣ Nested Loop (Brute Force – No inbuilt)
arr = [1, 2, 2, 3, 3, 4]
duplicates = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print(duplicates)


# 2️⃣ Fast lookup problem
nums = [1, 2, 3, 4]
seen = set()
for x in nums:
    if x in seen:
        print("Duplicate found")
    seen.add(x)
print(nums)



# 3️⃣ Two Sum (classic DSA)
nums = [2, 7, 11, 15]
target = 9
seen = set()
for x in nums:
    if target - x in seen:
        print("Found")
        break
    seen.add(x)


# 1️⃣ Set ka main purpose (MOST IMPORTANT)
# Fast lookup + uniqueness
# if x in my_set:   # O(1)
# Ye cheez 100% aani chahiye.

# 2️⃣ Set create karna + add karna
s = set()
s.add(5)

# Loop ke andar add karna (very common):
seen = set()
for x in arr:
    seen.add(x)

# 3️⃣ Duplicate detect karna (CORE DSA use)
seen = set()
for x in arr:
    if x in seen:
        print("Duplicate found")
        break
    seen.add(x)
# Used in:
# contains duplicate
# cycle detection
# visited tracking

# 4️⃣ Remove duplicates from array
unique = list(set(arr))

# (Interview me bolna: order lose hota hai)
# 5️⃣ Two Sum / Pair problems (VERY IMPORTANT)
# seen = set()
# for x in nums:
#     if target - x in seen:
#         return True
#     seen.add(x)


# Ye pattern bahut common hai.
# 6️⃣ Intersection of arrays
# a = set(arr1)
# b = set(arr2)
result = a & b
# Used in:
# common elements
# array comparison


# 7️⃣ Difference (Missing elements)
# missing = set(arr1) - set(arr2)

# 8️⃣ Visited tracking (Graph / DFS / BFS)
visited = set()

# if node not in visited:
#     visited.add(node)



















































