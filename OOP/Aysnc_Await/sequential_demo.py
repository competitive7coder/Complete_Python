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

# 🔑 What this means
# task1() is awaited fully
# Only after it finishes does task2() start
# No overlap at all
# 🕒 TIMELINE
# t = 0s → task1 starts
# t = 0–2s → task1 sleeping
# t = 2s → task1 finishes
# t = 2s → task2 starts
# t = 2–4s → task2 sleeping
# t = 4s → task2 finishes
# t = 4s → "both tasks completed"
#
# ⏱ Total time ≈ 4 seconds
