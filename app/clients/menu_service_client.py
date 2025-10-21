from typing import Type, TypeVar

import httpx
from pydantic import TypeAdapter

from app.models.product import Product
from app.models.upsell import Upsell

T = TypeVar("T")


class MenuServiceClient:
    def __init__(self, http: httpx.AsyncClient) -> None:
        self._http = http

    async def _fetch_list(self, endpoint: str, type_: Type[T]) -> list[T]:
        response = await self._http.get(endpoint)
        response.raise_for_status()
        result = response.json()
        ta = TypeAdapter(list[type_])  # type: ignore[valid-type]
        return ta.validate_python(result)

    async def get_products(self) -> list[Product]:
        return await self._fetch_list("/products.json", Product)

    async def get_upsells(self) -> list[Upsell]:
        return await self._fetch_list("/upsells.json", Upsell)
