# ******************************************************
"""TOPIC==>  isinstance() **Interview favorite.
class Student:
    pass
s1 = Student()
print(isinstance(s1, Student))
True (Output)"""
# ******************************************************

# ******************************************************
"""class Student:
    pass
s1 = Student()
s2 = Student()
print(s1 == s2)
False (Because they are two different objects)"""
# ******************************************************

# ******************************************************
"""class Student:
    pass
s1 = Student()
s2 = s1
print(s1 == s2)
True (Because both variables point to the same object)"""

# ******************************************************

# ******************************************************
class Student:
#__init__() is a special method called automatically when an object is created.
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Raj","BTECH/IT/23/110")
print(f"Student name is: {s1.name}")
print(f"Student roll number is: {s1.roll}")
s2 = Student("Protyush","BTECH/IT2/23/110")
print(f"Student name is: {s2.name}")
print(f"Student roll number is: {s2.roll}")

#********************************************************
#********************************************************
"""Instance Variables
Variables belonging to an object.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Here:
self.name
self.age
are instance variables"""
#********************************************************
