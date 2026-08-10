import os

# file_path = "abc.txt"
# file_path = "Encapsulation/main.py" // Wrong will give full path
# file_path = "../Encapsulation/main.py"

file_path = "C:\\Users\\proty\\OneDrive\\Complete ReactJS\\DocChain\\ALL_DETAILS.md"
#Absolute Path -- either use \\ or /

if os.path.isdir(file_path):
    print(f"'{file_path}' is a directory")
elif os.path.isfile(file_path):
    print(f"'{file_path}' is a file")
elif os.path.exists(file_path):
    print(f"'{file_path}' exists (but is neither a file nor a directory)")
else:
    print(f"The location '{file_path}' does not exist")
# If you want to specifically check for a file (not a folder)

# import os
# file_path = "abnc.txt"
# if os.path.isfile(file_path):
#     print(f"File '{file_path}' exists")
# else:
#     print(f"File '{file_path}' does not exist")

import os
file_path = r"C:\Users\proty\PycharmProjects\Python2025\PY_BASICS\OOP\Encapsulation\main.py"
print(os.path.isfile(file_path))
