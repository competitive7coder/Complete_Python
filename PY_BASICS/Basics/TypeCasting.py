# Typecasting in Python means converting one data type into another.

#1. int() → convert to integer
x = "10"
y = int(x)
print(y)
print(type(y))



#2. float() → convert to decimal
x = "10.5"
y = float(x)
print(y)        # 10.5
print(type(y))



#3. str() → convert to string
x = 10
y = str(x)

print(y)        # "10"
print(type(y))  # <class 'str'>



#4. bool() → convert to boolean
bool(0)      # False
bool(1)      # True
bool("")     # False
bool("hi")   # True


#input() always returns a string:
age = input("Enter your age: ")
#age = int(input("Enter your age: "))
print(type(age))  # str
# print(age + 5)  # ERROR
age = int(age)
print(age + 5)

#Example...............
age1 = input("Enter first number: ")
age2 = input("Enter second number: ")
print(age1 + age2)


