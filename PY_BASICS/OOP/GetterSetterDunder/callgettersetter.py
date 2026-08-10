from gettersetter import Bike, Bike1

b = Bike("Z900", 10)
print(b.get_price())
# b.set_price(-5)        # Invalid price
# b.set_price(12)
# print(b.get_price())
print(b.old)

b1 = Bike1("Z900", 10)
b1.set_price(12)
print(b1.price)
# b1.set_price(-5)        # Invalid price
# b1.set_price(12)
# print(b1.get_price())