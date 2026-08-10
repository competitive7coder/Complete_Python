#   ****** THESE ARE INSTANCE METHODS ******
class Car:
    # old = 2001
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

#   ****** THESE ARE INSTANCE METHODS ******

class Bike:
    old = 2001
# __init__ → special method(constructor),automatically called
# self → current object ka reference
    def __init__(self, brand, cc, price):
        self.brand = brand
        self.cc = cc
        self.price = price

    def drive(self):
        print(f"You are driving {self.brand}")

    def upgrade_cc(self, new_cc):
            self.cc = new_cc
            print(f"{self.brand} new cc is {self.cc}")

    def describe(self):
        print(f"my car specifications : {self.brand}, {self.cc}cc, {self.price}")