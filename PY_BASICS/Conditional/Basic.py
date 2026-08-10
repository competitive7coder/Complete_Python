# age = int(input("Enter Number: "))
# if age >=18:
#     print("You Can Drive.")
# else:
#     print("You Cannot Drive.")
#
#
#
# name = input("Enter Your Name: ")
# if name == "":
#     print("You Didnt Type Your Name")
# else:
#     print(f"Hello! {name}")

weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 2)} {unit}")

else :
    print(f"{unit} is not valid")





