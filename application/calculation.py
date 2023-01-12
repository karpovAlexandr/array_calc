from asyncio import sleep


def short_calculations(nums: list) -> int:
    return sum(nums)


async def long_async_calculations(nums: list) -> int:
    await sleep(15)
    return sum(nums)
