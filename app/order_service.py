import logging

from app.agents.customer import Customer
from app.agents.waiter import Waiter
from app.models.order import Order


class OrderService:
    def __init__(
        self,
        *,
        order: Order,
        waiter_agent: Waiter,
        customer_agent: Customer,
        logger: logging.Logger,
    ) -> None:
        self._order = order
        self._waiter_agent = waiter_agent
        self._customer_agent = customer_agent
        self._logger = logger

    def _log_waiter_message(self, message: str) -> None:
        self._logger.info(f"Waiter ({self._waiter_agent.name}): {message}")

    def _log_customer_message(self, message: str) -> None:
        self._logger.info(
            f"Customer ({self._customer_agent.number}): {message}"
        )

    async def simulate(self) -> Order:
        customer_message = None

        while True:
            waiter_message = await self._waiter_agent.handle(
                message=customer_message, order=self._order
            )
            self._log_waiter_message(waiter_message)
            customer_message = await self._customer_agent.handle(
                message=waiter_message
            )
            if not customer_message:
                break
            self._log_customer_message(customer_message)

        return self._order
