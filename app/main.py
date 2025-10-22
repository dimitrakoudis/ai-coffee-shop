import asyncio

import httpx

from app.agents.customer import Customer
from app.agents.waiter import Waiter
from app.clients.menu_service_client import MenuServiceClient
from app.constants import MAIN_WAITER_NAME, MENU_SERVICE_BASE_URL
from app.logger import get_logger
from app.models.menu import Menu
from app.models.order import Order
from app.order_service import OrderService

logger = get_logger(__name__)


async def main() -> None:
    logger.info("Starting simulation.")

    async with httpx.AsyncClient(base_url=MENU_SERVICE_BASE_URL) as menu_http:
        client = MenuServiceClient(menu_http)
        menu = Menu(
            products=await client.get_products(),
        )

    main_waiter = Waiter(name=MAIN_WAITER_NAME, menu=menu)

    order_service = OrderService(
        order=Order(),
        waiter_agent=main_waiter,
        customer_agent=Customer(
            number="#1",
            menu=menu,
            next_drink_names=["Non-existing", "Espresso"],
        ),
        logger=logger,
    )

    order = await order_service.simulate()
    logger.info(f"Order {order.order_id}: {order.total} EUR")

    logger.info("Finished simulation.")


if __name__ == "__main__":
    asyncio.run(main())
