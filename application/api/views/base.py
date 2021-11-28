import asyncio
from abc import ABCMeta, abstractmethod, ABC

from aiohttp import web


class BaseView(web.View, metaclass=ABCMeta):
    ENDPOINT: str

    def _from_query(self, parameter, is_optional=False):
        value = self.request.rel_url.query.get(parameter)
        if not value and not is_optional:
            raise web.HTTPBadRequest(reason=f"{value} is required")
        return value

    async def _from_body(self, parameter, is_optional=False):
        body = await self.request.json()
        value = body.get(parameter)
        if not value and not is_optional:
            raise web.HTTPBadRequest(reason=f"{value} is required")
        return value

    @abstractmethod
    async def compute(self) -> dict:
        pass


class GetView(BaseView, ABC):

    async def get(self):
        # use only compute function to simplify async-await logic
        response = await self.compute()
        return web.json_response(response)


class ThreadGetView(BaseView, ABC):

    async def handle_request(self):
        # use sync function as compute
        response = await asyncio.to_thread(self.compute)
        return response

    async def get(self):
        response = await self.handle_request()
        return web.json_response(response)
