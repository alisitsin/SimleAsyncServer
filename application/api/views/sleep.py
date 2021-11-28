import asyncio
import time

from .base import GetView, ThreadGetView


class SleepView(GetView):
    ENDPOINT = "/sleep"

    async def compute(self):
        sleep = self._from_query("sleep")
        # that sleep blocks
        time.sleep(int(sleep))
        return {"sleep": sleep}


class AsyncSleepView(GetView):
    ENDPOINT = "/async-sleep"

    async def compute(self):
        sleep = self._from_query("sleep")
        # awaitable sleep
        await asyncio.sleep(int(sleep))
        return {"async-sleep": sleep}


class ThreadSleepView(ThreadGetView):
    ENDPOINT = "/thread-sleep"

    # compute function is sync now
    def compute(self):
        sleep = self._from_query("sleep")
        name = self._from_query("name", is_optional=True)
        print(f"'{name}': start sleeping at {time.strftime('%X')}")
        time.sleep(int(sleep))
        print(f"'{name}': finish sleeping at {time.strftime('%X')}")
        return {"thread-sleep": sleep}

    # TODO: check how to_thread works with another manual thread
