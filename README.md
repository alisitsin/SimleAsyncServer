# Simple Async Service
This example shows the basic way to implement async server which can handle requests simultaneously.

It might be not really obvious that **aiohttp** does support async but doesn't support parallel handling out of the box.
Actually every async function should await some part of the code in it's body but this code should also be "awaitable" of course.


**From Python 3.9 asyncio** provides simple interface to execute your code in the new **awaitable** thread.
[See the description here](https://docs.python.org/3/library/asyncio-task.html?highlight=to_thread#id10)
Use pattie `.to_thread()` instead of handling all loops stuff by yourself.

This example shows principle difference between new the approach and the old one.

*Try*

1. Send different sleep requests
2. Try to reach status or other endpoint  

*Keywords*
aiohttp, asyncio, threads, threading, python3.9, parallel requests handling