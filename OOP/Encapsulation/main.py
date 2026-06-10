# ❌ Without encapsulation (BAD)
class Product:
    def __init__(self, price):
        self.price = price

p = Product(100)
p.price = -500   # ❌ allowed
# 💥 Bug created. No protection.

# ✅ With encapsulation (GOOD)
class Product:
    def __init__(self, price):
        self._price = price   # internal

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Invalid price")
        self._price = value


p = Product(100)
p.price = 200     # ✅
p.price = -50     # ❌ ValueError



# ✅ EXAMPLE 2: READ-ONLY ID (identity protection)
class User:
    def __init__(self, user_id):
        self._id = user_id

    @property
    def id(self):
        return self._id

u = User(10)

print(u.id)   # ✅ allowed
u.id = 20     # ❌ AttributeError


# ✅ EXAMPLE 3: BANK ACCOUNT (state protection)
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

acc = BankAccount(1000)
acc.deposit(500)     # ✅
acc.withdraw(200)    # ✅
acc.withdraw(5000)   # ❌
# ❌ No one can do:

acc._balance = -999999   # BAD PRACTICE
# ✔ State always valid



# EXAMPLE 6: PROTECTED METHOD (internal workflow)
class Service:
    def process(self):
        self._validate()
        print("processing done")

    def _validate(self):
        print("internal validation")

s = Service()
s.process()     # ✅ correct
s._validate()   # ⚠️ works, but DON’T