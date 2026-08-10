# Tuple = ordered + immutable collection
t = (10, 20, 30)
# Ordered → index hota hai
# Immutable → change nahi kar sakte
# “Tuple immutable hota hai isliye memory efficient aur safer hota hai.”


# 3️⃣ Indexing & Slicing (Aana hi chahiye)
t = (5, 10, 15, 20)
print(t[0])     # 5
print(t[-1])    # 20
print(t[1:3])   # (10, 15)
# Same as list — koi difference nahi.


# 4️⃣ Tuple IMMUTABLE kyun important hai (VERY IMPORTANT)
t = (1, 2, 3)
t[0] = 10   # ❌ TypeError
# DSA use:
# Data accidental change se safe
# Hashable → dict/set key ban sakta hai


# 5️⃣ Tuple as KEY (DSA GOLD POINT)
visited = set()
visited.add((2, 3))   # ✅ allowed
visited.add([2, 3])   # ❌ error
# Kyun?
# Tuple → immutable → hashable
# List → mutable → not hashable
# Used in:
# Grid problems
# Graph traversal
# DFS / BFS
# Memoization


# 6️⃣ Multiple values return karna (VERY COMMON)
def solve(arr):
    return min(arr), max(arr)
mn, mx = solve([3, 1, 5])
# Return value = tuple
# Interview me bol sakte ho:
# “Python me multiple return tuple ke through hota hai.”


# 7️⃣ Unpacking (DSA me bahut use hota hai)
a, b = (10, 20)
# Swap trick:
a, b = b, a
# No temp variable → clean DSA trick


# 8️⃣ Enumerate / Zip ke saath tuple
arr = [10, 20, 30]
for i, val in enumerate(arr):
    print(i, val)
# Behind the scenes:
# (i, val)  # tuple


# 9️⃣ Looping over tuple
t = (1, 2, 3)
for x in t:
    print(x)
# Index-based:
for i in range(len(t)):
    print(t[i])

# 🔟 Tuple methods (Bas itna hi kaafi hai)
t.count(10)
t.index(20)


# 1️⃣1️⃣ Tuple kab use karein? (INTERVIEW ANSWER)
# Use tuple when:
# Data fixed hai
# Coordinate / pair store karna ho
# Dictionary / set key banana ho
# Accidental modification avoid karni ho
# Use list when:
# Insert / delete / modify karna ho



