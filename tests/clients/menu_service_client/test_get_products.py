from decimal import Decimal

import pytest

from app.clients.menu_service_client import MenuServiceClient
from app.models.categories import Category
from app.models.product import Product
from tests.conftest import TEST_MENU_SERVICE_BASE_URL


@pytest.mark.asyncio
async def test_success_200(httpx_mock, menu_service_client: MenuServiceClient):
    httpx_mock.add_response(
        url=f"{TEST_MENU_SERVICE_BASE_URL}/products.json",
        status_code=200,
        json=[
            {"name": "a", "price": 1, "category": "basic"},
            {"name": "b", "price": 2, "category": "basic"},
        ],
    )

    actual = await menu_service_client.get_products()
    expected = [
        Product(name="a", price=Decimal("1"), category=Category.BASIC),
        Product(name="b", price=Decimal("2"), category=Category.BASIC),
    ]
    assert actual == expected
