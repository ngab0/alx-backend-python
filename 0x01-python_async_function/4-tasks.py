#!/usr/bin/env python3
""" 4-tasks module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times with the specified max_delay and returns
    the list of all the delays (float values) in ascending order
    """
    delays = await asyncio.gather(
      *[task_wait_random(max_delay) for i in range(n)])
    return sorted(delays)
