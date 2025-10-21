import asyncio

import httpx

from app.clients.menu_service_client import MenuServiceClient
from app.constants import MENU_SERVICE_BASE_URL
from app.logger import get_logger

logger = get_logger(__name__)


async def main() -> None:
    logger.info("Starting simulation.")

    async with httpx.AsyncClient(base_url=MENU_SERVICE_BASE_URL) as menu_http:
        client = MenuServiceClient(menu_http)
        products = await client.get_products()
        upsells = await client.get_upsells()

        logger.info(f"Products: {products}")
        logger.info(f"Upsells: {upsells}")

    logger.info("Finished simulation.")


if __name__ == "__main__":
    asyncio.run(main())
