import asyncio
async def task1():
    await asyncio.sleep(2)
    print("task1 done after 2 seconds")
async def task2():
    await asyncio.sleep(2)
    print("task2 done after 2 seconds")
async def main():
    # t1 = asyncio.create_task(task1())
    # t2 = asyncio.create_task(task2())
    # await asyncio.gather(t1, t2)
    await asyncio.gather(task1(), task2())

    print("both tasks completed")

asyncio.run(main())

# 🔑 What this means
# create_task() starts the coroutine immediately
# Both task1 and task2 are scheduled at the same time
# await asyncio.gather(...) waits for both together

# 🕒 TIMELINE (IMPORTANT)
# t = 0s → task1 starts
# t = 0s → task2 starts
# t = 0–2s → BOTH waiting (sleep)
# t = 2s → task1 finishes
# t = 2s → task2 finishes
# t = 2s → "both tasks completed"
#
# ⏱ Total time ≈ 2 seconds