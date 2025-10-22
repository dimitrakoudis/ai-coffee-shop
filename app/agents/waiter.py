from app.agents import constants
from app.models.menu import Menu
from app.models.order import Order


# Not covering with tests, given we'd use a real agent instead.
class Waiter:  # pragma: no cover
    def __init__(
        self,
        *,
        name: str,
        menu: Menu,
    ) -> None:
        self._name = name
        self._menu = menu

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def _extract_product_name_from_message(message: str) -> str:
        """
        Extracts the product name from a customer message,
        assuming all product names are in Title Case.
        """
        return (
            message.split(constants.I_WOULD_LIKE_MESSAGE)[-1]
            .lstrip("an ")
            .lstrip("a ")
            .strip(" ")
            .rstrip(".")
            .title()
        )

    @staticmethod
    def _is_message_that_is_all(message: str) -> bool:
        return message == constants.THAT_IS_ALL_MESSAGE

    @staticmethod
    def _is_message_an_add_product(message: str) -> bool:
        return constants.I_WOULD_LIKE_MESSAGE in message

    @staticmethod
    def _is_message_need_more_time(message: str) -> bool:
        return message == constants.NEED_MORE_TIME_MESSAGE

    @staticmethod
    def _is_message_need_the_drink_menu(message: str) -> bool:
        return message == constants.NEED_THE_DRINK_MENU_MESSAGE

    async def handle(self, *, message: str | None, order: Order) -> str:
        if not message:
            return constants.WELCOME_MESSAGE

        if self._is_message_need_the_drink_menu(message):
            return constants.WILL_BRING_YOU_THE_MENU_MESSAGE

        if self._is_message_need_more_time(message):
            return constants.TAKE_YOUR_TIME_MESSAGE

        is_add_product = self._is_message_an_add_product(message)
        if is_add_product:
            product_name = self._extract_product_name_from_message(message)
            product = self._menu.get_product_by_name(product_name)

            if not product:
                return constants.PRODUCT_NOT_FOUND_MESSAGE

            order.add_product(product)
            return constants.ANYTHING_ELSE_MESSAGE

        if self._is_message_that_is_all(message):
            total = order.total
            if not total:
                return constants.GOODBYE_MESSAGE
            return constants.GOODBYE_WITH_TOTAL_MESSAGE.format(total=total)

        return constants.I_DONT_UNDERSTAND_MESSAGE
