# Dictionary = key–value pair ka collection
d = {
    "a": 1,
    "b": 2
}
# Key → unique hoti hai
# Value → kuch bhi ho sakta hai
# Order preserved (Python 3.7+)
# Fast lookup + counting + mapping
# Lookup: O(1) average
# Counting: frequency problem
# Mapping: value ko kisi key se relate karna

# 1️⃣ Dictionary banana
freq = {}
freq = dict()


# 2️⃣ Add / Update values
freq["a"] = 1
freq["a"] += 1


# Common DSA pattern:
arr = [10,20,30]
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# 3️⃣ Access value (MOST USED)
print(freq["a"])


# Safe access (no error):
# dict.get(key, default)
print(freq.get("a", 0))# 0 is default value
#Output:3
freq = {}
print(freq.get("a", 0)) #Output:0



# Interview tip: get() avoids KeyError.
# 4️⃣ Frequency count (DSA GOLD)
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)
# Output:
{1: 1, 2: 2, 3: 3}


# Used in:
# majority element
# most frequent element
# anagrams
# counting problems


# 5️⃣ Looping in dictionary
for k in freq:
    print(k, freq[k])


# Or:
for k, v in freq.items():
    print(k, v)

# 6️⃣ Membership check (O(1))
if 3 in freq:
    print("exists")

# 7️⃣ Dictionary as hash map (DSA term)
# Python dict = HashMap
# Used in:
# Two Sum
# Index mapping
# Fast searching


# Example (Two Sum):
nums = [2, 7, 11, 15]
target = 9
mp = {}

for i in range(len(nums)):
    need = target - nums[i]
    if need in mp:
        print(mp[need], i)
        break
    mp[nums[i]] = i

# 8️⃣ Keys must be immutable (IMPORTANT)
# Allowed keys:
(1, 2)     # tuple
"abc"
10

# Not allowed:
[1, 2]     # list ❌
# Reason:
# Keys must be hashable (immutable)
