class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, level):
        # self.name = name       # duplicate logic
        super().__init__(name) # User have only name arg passing
        self.level = level

    def show_role(self):
        print(f"{self.name} is an {self.level}")

a = Admin("RAJ", "Admin")
print(a.name)
a.show_role()


class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
d = Dog("Tommy", "Labrador")
print(d.name)
print(d.breed)
