from collections.abc import AsyncGenerator

import httpx
import pytest
import pytest_asyncio
from faker.proxy import Faker

from app.agents.customer import Customer
from app.agents.waiter import Waiter
from app.clients.menu_service_client import MenuServiceClient
from app.logger import get_logger
from app.models.menu import Menu
from app.models.order import Order
from app.order_service import OrderService

faker = Faker()
TEST_MENU_SERVICE_BASE_URL = "http://localhost/api/menu-service"


@pytest_asyncio.fixture()
async def menu_service_client() -> AsyncGenerator[MenuServiceClient]:
    async with httpx.AsyncClient(base_url=TEST_MENU_SERVICE_BASE_URL) as http:
        yield MenuServiceClient(http)


@pytest.fixture()
def menu() -> Menu:
    return Menu(
        products=[],
    )


@pytest.fixture()
def customer_agent(menu: Menu) -> Customer:
    return Customer(
        number=faker.uuid4(),
        menu=menu,
        next_drink_names=None,
    )


@pytest.fixture()
def waiter_agent(menu: Menu) -> Waiter:
    return Waiter(
        name=faker.name(),
        menu=menu,
    )


@pytest.fixture()
def empty_order() -> Order:
    return Order()


@pytest.fixture()
def order_service(
    empty_order: Order,
    waiter_agent: Waiter,
    customer_agent: Customer,
) -> OrderService:
    return OrderService(
        order=empty_order,
        waiter_agent=waiter_agent,
        customer_agent=customer_agent,
        logger=get_logger("tests"),
    )
