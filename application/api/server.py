from aiohttp import web

from .views import VIEWS


class Server:
    def __init__(self, port=8005, host="localhost"):
        self.port = port
        self.host = host
        self.app = web.Application()

    @staticmethod
    async def welcome(request):
        return web.HTTPOk(text="Hello there!")

    def run(self):
        print(f"Run server")
        self.app.add_routes([web.get("/", self.welcome)])

        for view in VIEWS:
            self.app.router.add_route("*", view.ENDPOINT, view)

        web.run_app(self.app, host=self.host, port=self.port)
