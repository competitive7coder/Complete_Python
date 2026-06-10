# 🔁 SAME IDEA, REAL-WORLD STYLE (LOGGER EXAMPLE)
# ⚡ FASTAPI CONNECTION (VERY IMPORTANT)
class UserService:
    def process(self):
        print("User logic")

class AdminService:
    def process(self):
        print("Admin logic")

def route(service):
    service.process()

route(UserService())
route(AdminService())


class Dog:
    def speak(self):
        return "Bark"
class Cat:
    def speak(self):
        return "Meow"
class Robot:
    def speak(self):
        return "Beep"

animals = [Dog(), Cat(), Robot()]
for animal in animals:
    print(animal.speak())

