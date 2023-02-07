#!/usr/bin/env python3
""" 1-concurrent_coroutines module"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times with the specified max_delay and
    returns the list of all the delays (float values) in ascending order
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for i in range(n)])
    return sorted(delays)
