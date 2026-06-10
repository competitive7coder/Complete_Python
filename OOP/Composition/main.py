# ===== TIGHT COMPOSITION START =====

class Engine:
    def start(self):
        print("Engine started")


class CarTight:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is moving")


print("\n--- TIGHT COMPOSITION OUTPUT ---")
car1 = CarTight()
car1.drive()
print("--- TIGHT COMPOSITION END ---\n")


# ===== LOOSE COMPOSITION / DEPENDENCY INJECTION START =====

class PetrolEngine:
    def start(self):
        print("Petrol engine started")

class ElectricEngine:
    def start(self):
        print("Electric engine started")

class CarLoose:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is moving")


print("--- LOOSE COMPOSITION OUTPUT ---")
engine1 = PetrolEngine()
engine2 = ElectricEngine()
#car2 = CarLoose(PetrolEngine())
car2 = CarLoose(engine1)
car3 = CarLoose(engine2)

car2.drive()
car3.drive()
print("--- LOOSE COMPOSITION END ---")
