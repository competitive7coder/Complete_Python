# for x in range(1,10,2):
#     print(x)



# name = "PROTYUSH"
# for i in name:
#     print(i)



# import time
# for x in range(1,20):
#     if x%2 == 0:
#         time.sleep(4)
#     else:
#         print(x)



# import time
# my_time = int(input("Enter Time in Seconds: "))
#
# for i in reversed(range(0,my_time +  1)):
#     print(i)
#     time.sleep(1)
# print("TIMES UP!")



import time
my_time = int(input("Enter Time in Seconds: "))

for i in (range(my_time, 0, -1)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIMES UP!")



