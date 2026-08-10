# 5️⃣ Polymorphism via Inheritance (MOST COMMON)
class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def area(self):
        return 10 * 5
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
# Usage
shapes = [Rectangle(), Circle()]
for s in shapes:
    print(s.area())
# Output:
# 50
# 78.5


# 6️⃣ Method Overriding = Polymorphism
class User:
    def role(self):
        return "user"
class Admin(User):
    def role(self):
        return "admin"
users = [User(), Admin()]
for u in users:
    print(u.role())




class Animal:
    def eyes(self):
        return "Animal Has 2 Eyes"
class Human(Animal):
    def eyes(self):
        return "Human Has 2 Eyes"
class Bird(Animal):
    def eyes(self):
        return "Bird Has 2 Eyes"

e = [Animal(), Human(), Bird()]
for i in e:
    print(i.eyes())
"""
if use print instead of return like print("Animal Has 2 Eyes")
Now x = h.eyes(). Python goes inside eyes(). print("Human Has 2 Eyes")
So immediately it prints: Human Has 2 Eyes. Then the function ends.
Since there is no return, Python does:
return None
So now: x = None
Nothing else is printed yet.
"""