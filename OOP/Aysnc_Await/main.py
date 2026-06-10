# import time
# def task():
#     time.sleep(2)
#     print("task done")
# def main():
#     task()
#     print("end")
# main()
# import time
# import asyncio
# async def task():
#     await asyncio.sleep(2)
#     print("task done")
# async def main():
#     await task()
#     print("end")
# asyncio.run(main()) # Event Loop is created,,,,,Loop takes control of program
# import asyncio
# async def task1():
#     await asyncio.sleep(2)
#     print("task1 done after 2 seconds")
# async def task2():
#     await asyncio.sleep(2)
#     print("task2 done after 2 seconds")
# async def main():
#     t1 = asyncio.create_task(task1())
#     t2 = asyncio.create_task(task2())
#     await asyncio.gather(t1, t2)
#     print("both tasks completed")
# asyncio.run(main())

import asyncio
async def task1():
    print("task1 started")
    await asyncio.sleep(2)
    print("task1 finished after 2 seconds")
async def task2():
    print("task2 started")
    await asyncio.sleep(2)
    print("task2 finished after 2 seconds")
async def main():
    await task1()   # waits full 2 seconds
    await task2()   # starts only after task1 ends

    print("both tasks completed")

asyncio.run(main())
