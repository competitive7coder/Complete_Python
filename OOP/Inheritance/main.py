class Animal:
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print(f"{self.name} barks")

class Dog(Animal):
    pass

class Cat(Animal):
    def eat(self):
        print(f"{self.name} eats")
d = Dog("Scooby")
d.sleep()    # own
c = Cat("Micky")
c.sleep()
c.eat()

# 5️⃣ super() — PARENT KO CALL KARNA
class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, level):
        #self.name = name   ##duplicate logic
        super().__init__(name)
        self.level = level

# 9️⃣ TYPES OF INHERITANCE IN PYTHON

# 1️⃣ Single Inheritance (MOST COMMON)
class A: ...
class B(A): ...

# 2️⃣ Multilevel Inheritance
class A: ...
class B(A): ...
class C(B): ...

# 3️⃣ Multiple Inheritance (DANGEROUS)
class A: ...
class B: ...
class C(A, B): ...