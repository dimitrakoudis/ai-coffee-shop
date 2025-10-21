from collections.abc import AsyncGenerator

import httpx
import pytest_asyncio

from app.clients.menu_service_client import MenuServiceClient

TEST_MENU_SERVICE_BASE_URL = "http://localhost/api/menu-service"


@pytest_asyncio.fixture()
async def menu_service_client() -> AsyncGenerator[MenuServiceClient]:
    async with httpx.AsyncClient(base_url=TEST_MENU_SERVICE_BASE_URL) as http:
        yield MenuServiceClient(http)
