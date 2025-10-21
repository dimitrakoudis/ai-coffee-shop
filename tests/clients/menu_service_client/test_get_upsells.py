import pytest

from app.clients.menu_service_client import MenuServiceClient
from app.models.categories import Category
from app.models.upsell import Upsell, WhenToUpsell
from tests.conftest import TEST_MENU_SERVICE_BASE_URL


@pytest.mark.asyncio
async def test_success_200(httpx_mock, menu_service_client: MenuServiceClient):
    httpx_mock.add_response(
        url=f"{TEST_MENU_SERVICE_BASE_URL}/upsells.json",
        status_code=200,
        json=[
            {
                "name": "up1",
                "try_per_order": 1,
                "item_to_upsell": "p1",
                "when": {"category_ordered": ["coffee", "tea"]},
            },
            {
                "name": "up2",
                "try_per_order": 2,
                "item_to_upsell": "p2",
                "when": {"category_ordered": ["soft drink"]},
            },
        ],
    )

    actual = await menu_service_client.get_upsells()
    expected = [
        Upsell(
            name="up1",
            try_per_order=1,
            item_to_upsell="p1",
            when=WhenToUpsell(
                category_ordered=[Category.COFFEE, Category.TEA],
            ),
        ),
        Upsell(
            name="up2",
            try_per_order=2,
            item_to_upsell="p2",
            when=WhenToUpsell(
                category_ordered=[Category.SOFT_DRINK],
            ),
        ),
    ]
    assert actual == expected
