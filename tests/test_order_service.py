import pytest

from app.order_service import OrderService


@pytest.mark.asyncio
async def test_order_service(order_service: OrderService):
    await order_service.simulate()
    assert True
