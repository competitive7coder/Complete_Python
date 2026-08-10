sum = 0
arr = [10,20,30,40]
print("Your given array is: ")
for i in arr:
    print(i)

for i in range(len(arr)):
    sum+= arr[i]
print(f"Sum of array is: {sum}")
