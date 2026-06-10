# import car    Import full module
from car import Car, Bike

my_car1 = Car("BMW", 2025, "Black", True)
print(my_car1.year, my_car1.model)
my_car2 = Car("TOYOTA SUPRA", 2018, "White", False)
print(my_car2.year, my_car2.for_sale)

my_bike = Bike("Z900", 900, "10Lakhs")
print(my_bike.brand, my_bike.cc, my_bike.price)
my_bike.drive()
my_bike.upgrade_cc(1000)
my_bike.describe()