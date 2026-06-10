# Syntax: while(condition):

# i = 0
# while i<=5:
#     print(i)
#     i = i + 1





# name = input("Enter Your Name: ")
# while name == "":
#     print("You did not type your name.")
#     name = input("Enter Your Name: ")
# print(f"Hello, {name}")





while True:
    age_input = input("Enter Your Age: ")

    if age_input.strip() == "":
        # if i do age_input== "" then if user do input multiple spaces then
        # it count it as string, fails 1st condition checks
        #thats why i use .strip()
        print("Age cannot be empty.")
        continue

    if not age_input.isdigit():
        print("Please enter a valid number.")
        continue

    age = int(age_input)

    if age < 0:
        print("Age cannot be negative.")
        continue

    break

print(f"Hello, {age}")





