import asyncio
import sys

async def loading_spinner(label: str, stop_event: asyncio.Event):
    frames = ["|", "/", "-", "\\"]
    i = 0
    while not stop_event.is_set():
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r{label} {frame}")
        sys.stdout.flush()
        i += 1
        await asyncio.sleep(0.1)
    sys.stdout.write(f"\r{label} done\n")
    sys.stdout.flush()

async def work(seconds: float):
    await asyncio.sleep(seconds)

async def run_with_spinner(label: str, coroutine):
    # make flag
    stop_event = asyncio.Event()
    # start spinner
    spinner = asyncio.create_task(loading_spinner(label, stop_event))
    # simultaneously run the coroutine
    await coroutine
    # coroutine finished, stop spinner
    stop_event.set()
    # wait for spinner to finish
    await spinner

async def main():
    await run_with_spinner("Fetching data...", work(5))
    await run_with_spinner("Processing...",    work(2.5))
    await run_with_spinner("Saving results...", work(1))

asyncio.run(main())