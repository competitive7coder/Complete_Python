# Function = reusable block of code jo ek kaam karta hai.
def greet():
    print("Hello")
# def → function define karne ka keyword
# greet → function name
# () → parameters (abhi empty)
# : → function body start
# Call:
greet()


# 1️⃣ Parameters & Arguments (VERY IMPORTANT)
# Parameter = function ke andar variable
# Argument = function call ke time value
def square(x):     # x = parameter
    return x * x

print(square(5))  # 5 = argument


# 2️⃣ return keyword (CORE CONCEPT)
def add(a, b):
    return a + b
ans = add(10,20)
print(ans)
# print(add(10,20)) # sirf print karta hai, store nahi


# 3️⃣ Function without return
def show(a):
    print(a)
# Calling:
x = show(10)
print(x)   # None
# 👉 Agar return nahi likha → None milta hai.


# 4️⃣ Multiple return values (Tuple concept)
def min_max(arr):
    return min(arr), max(arr)
mn, mx = min_max([3, 1, 5])
# Return actually:
print((min, max))  # tuple => (<built-in function min>, <built-in function max>)


# 5️⃣ Default Parameters
def power(x, p=2):
    return x ** p
print(power(3))     # 3 square => 9
print(power(3, 3))  # 3 cube => 27
# DSA me useful jab optional input ho.


# 6️⃣ Passing List to Function (DSA GOLD)
# List mutable hoti hai
def change(arr):
    arr.append(100)
nums = [1, 2, 3]
change(nums)
print(nums)   # [1,2,3,100]
# 👉 Function original list change kar sakta hai.
# Agar original safe rakhna ho

def change(arr):
    arr = arr.copy()
    arr.append(100)
    return arr


# 7️⃣ Function ke andar loop + condition (Most common)
def find_max(arr):
    mx = arr[0]
    for x in arr:
        if x > mx:
            mx = x
    return mx
# Used in:
# max/min
# searching
# counting
# validation


# 8️⃣ Function for DSA pattern (Example)
def has_duplicate(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False
# Interview-ready logic 👍


# 9️⃣ Scope (Local vs Global) – BASIC
x = 10

def test():
    x = 5
    print(x)

test()
print(x)
# Output:
5
10


# 👉 Function ke andar ka x alag hota hai.
# 🔟 Function naming (Interview tip)
# lowercase
# meaningful
# verbs preferred
# example
# find_max
# count_freq
# is_valid



# Default Arguments
# 👉 Parameter ki default value hoti hai

def power(x, p=2):
    return x ** p

print(power(3))     # 9
print(power(3, 3))  # 27
# Agar argument pass nahi kiya → default use hoga
# Agar pass kiya → default overwrite
# Rule (IMPORTANT)
# Default arguments hamesha last me aate hain:
def f(a, b=10):   # ✅
    pass
# def f(a=10, b):  # ❌ error
    pass




# 3️⃣ Keyword Arguments
# 👉 Parameter ka naam use karke value pass karna
def student(name, age):
    print(name, age)
student(age=20, name="Raj")
# Output:
# Raj 20
# Mix allowed
# student("Raj", age=20)   # ✅
#
# ❌ But:
# student(name="Raj", 20)  # ❌ positional after keyword not allowed




# 5️⃣ Arbitrary Keyword Arguments (**kwargs)
# 👉 Jab key=value pairs unknown ho

def info(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

info(name="Raj", age=20, city="Kolkata")
# kwargs = dictionary



# 🔥 MOST IMPORTANT ORDER RULE (Interview Favorite)
# def func(positional, default=0, *args, **kwargs):
#     pass

# Order hamesha:
# positional
# default
# *args
# **kwargs