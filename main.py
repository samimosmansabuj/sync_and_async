import time
import asyncio

# Synchronous
def download_file_sync(filename):
    print(f"{filename} Download Start..")
    time.sleep(2)
    print(f"{filename} Download Complete...")

def main_sync():
    download_file_sync("file1.txt")
    download_file_sync("file2.txt")
    download_file_sync("file3.txt")

print(main_sync())
# ⏱️ সময় লাগবে প্রায় ৬ সেকেন্ড (২+২+২)।

#Using Asynchronous
async def download_file_async(filename):
    print(f"{filename} Download Start...")
    await asyncio.sleep(2)
    print(f"{filename} Download Complete...")

async def main_async():
    tasks = [
        download_file_async("file1.txt"),
        download_file_async("file2.txt"),
        download_file_async("file3.txt")
    ]
    await asyncio.gather(*tasks)

asyncio.run(main_async())
# ⏱️ সময় লাগবে মোটামুটি ২ সেকেন্ড — কারণ সবগুলো একসাথে চলে।
