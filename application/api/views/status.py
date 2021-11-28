from .base import GetView


class StatusView(GetView):
    ENDPOINT = "/status"

    async def compute(self):
        return {"status": "OK"}
