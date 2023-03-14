#!/usr/bin/env python3
""" Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself. """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function that measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
